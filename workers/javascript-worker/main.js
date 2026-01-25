const express = require('express');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const app = express();
app.use(express.json());

const MAX_TIME_MS = 10000;

function executeJavaScript(code, testCases, entryPoint, timeoutMs) {
  return new Promise((resolve) => {
    const results = [];
    let compileError = null;
    let runtimeError = null;

    const timeout = Math.min(timeoutMs || 5000, MAX_TIME_MS);

    const runTest = async (index) => {
      if (index >= testCases.length) {
        resolve({ results, compile_error: compileError, runtime_error: runtimeError });
        return;
      }

      const test = testCases[index];
      const testName = test.name || `test_${index}`;
      const testInput = test.input || '';
      const expectedOutput = test.expected_output || '';

      let testCode;
      if (entryPoint) {
        // Function-based test
        testCode = `
${code}

const args = JSON.parse('${JSON.stringify(testInput)}');
let result;
if (Array.isArray(args)) {
  result = ${entryPoint}(...args);
} else {
  result = ${entryPoint}(args);
}
console.log(typeof result === 'object' ? JSON.stringify(result) : result);
`;
      } else {
        testCode = code;
      }

      const tempFile = path.join(os.tmpdir(), `js_${Date.now()}_${index}.js`);

      try {
        fs.writeFileSync(tempFile, testCode);

        const child = spawn('node', [tempFile], {
          timeout: timeout,
          stdio: ['pipe', 'pipe', 'pipe']
        });

        let stdout = '';
        let stderr = '';

        child.stdout.on('data', (data) => {
          stdout += data.toString();
        });

        child.stderr.on('data', (data) => {
          stderr += data.toString();
        });

        const timeoutId = setTimeout(() => {
          child.kill('SIGKILL');
        }, timeout);

        child.on('close', (exitCode) => {
          clearTimeout(timeoutId);

          try {
            fs.unlinkSync(tempFile);
          } catch (e) {}

          const actualOutput = stdout.trim();

          if (exitCode !== 0 && exitCode !== null) {
            results.push({
              name: testName,
              passed: false,
              expected: expectedOutput,
              actual: actualOutput,
              error: stderr || `Exit code: ${exitCode}`
            });
          } else if (child.killed) {
            results.push({
              name: testName,
              passed: false,
              expected: expectedOutput,
              actual: null,
              error: 'Execution timed out'
            });
          } else {
            const passed = actualOutput === expectedOutput.trim();
            results.push({
              name: testName,
              passed: passed,
              expected: expectedOutput,
              actual: actualOutput,
              error: stderr || null
            });
          }

          runTest(index + 1);
        });

        child.on('error', (err) => {
          clearTimeout(timeoutId);
          try {
            fs.unlinkSync(tempFile);
          } catch (e) {}

          results.push({
            name: testName,
            passed: false,
            expected: expectedOutput,
            actual: null,
            error: err.message
          });

          runTest(index + 1);
        });

        if (!entryPoint && testInput) {
          child.stdin.write(testInput);
          child.stdin.end();
        }

      } catch (err) {
        try {
          fs.unlinkSync(tempFile);
        } catch (e) {}

        if (err instanceof SyntaxError) {
          compileError = err.message;
          resolve({ results, compile_error: compileError, runtime_error: runtimeError });
        } else {
          results.push({
            name: testName,
            passed: false,
            expected: expectedOutput,
            actual: null,
            error: err.message
          });
          runTest(index + 1);
        }
      }
    };

    runTest(0);
  });
}

app.post('/execute', async (req, res) => {
  const { code, test_cases, entry_point, timeout_ms } = req.body;

  try {
    const result = await executeJavaScript(
      code || '',
      test_cases || [],
      entry_point,
      timeout_ms || 5000
    );
    res.json(result);
  } catch (err) {
    res.json({
      results: [],
      compile_error: null,
      runtime_error: err.message
    });
  }
});

app.get('/health', (req, res) => {
  res.json({ status: 'healthy', language: 'javascript' });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`JavaScript worker running on port ${PORT}`);
});
