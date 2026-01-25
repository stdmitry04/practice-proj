const express = require('express');
const { spawn } = require('child_process');
const fs = require('fs');
const path = require('path');
const os = require('os');

const app = express();
app.use(express.json());

const MAX_TIME_MS = 15000;

// Create a test runner template
const createTestRunner = (code, testCases, entryPoint) => {
  const testCode = testCases.map((test, idx) => `
    try {
      const result = (() => {
        ${test.input}
      })();
      const expected = ${JSON.stringify(test.expected_output)};
      const passed = JSON.stringify(result) === JSON.stringify(expected) || String(result) === expected;
      results.push({
        name: ${JSON.stringify(test.name || `test_${idx}`)},
        passed: passed,
        expected: expected,
        actual: typeof result === 'object' ? JSON.stringify(result) : String(result),
        error: null
      });
    } catch (err) {
      results.push({
        name: ${JSON.stringify(test.name || `test_${idx}`)},
        passed: false,
        expected: ${JSON.stringify(test.expected_output)},
        actual: null,
        error: err.message
      });
    }
  `).join('\n');

  return `
const React = require('react');
const { render, screen, fireEvent, waitFor } = require('@testing-library/react');
const { JSDOM } = require('jsdom');

// Setup DOM environment
const dom = new JSDOM('<!DOCTYPE html><html><body><div id="root"></div></body></html>', {
  url: 'http://localhost',
  pretendToBeVisual: true
});
global.window = dom.window;
global.document = dom.window.document;
global.navigator = dom.window.navigator;

// User's code
${code}

// Test execution
const results = [];

${testCode}

console.log(JSON.stringify({ results, compile_error: null, runtime_error: null }));
`;
};

function executeReactCode(code, testCases, entryPoint, timeoutMs) {
  return new Promise((resolve) => {
    const timeout = Math.min(timeoutMs || 10000, MAX_TIME_MS);

    const testRunnerCode = createTestRunner(code, testCases, entryPoint);
    const tempFile = path.join(os.tmpdir(), `react_${Date.now()}.js`);

    try {
      fs.writeFileSync(tempFile, testRunnerCode);

      const child = spawn('node', [tempFile], {
        timeout: timeout,
        stdio: ['pipe', 'pipe', 'pipe'],
        cwd: __dirname
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

        if (child.killed) {
          resolve({
            results: testCases.map((test, idx) => ({
              name: test.name || `test_${idx}`,
              passed: false,
              expected: test.expected_output,
              actual: null,
              error: 'Execution timed out'
            })),
            compile_error: null,
            runtime_error: 'Execution timed out'
          });
          return;
        }

        try {
          const result = JSON.parse(stdout.trim());
          resolve(result);
        } catch (parseErr) {
          // If we can't parse the output, there was likely an error
          resolve({
            results: testCases.map((test, idx) => ({
              name: test.name || `test_${idx}`,
              passed: false,
              expected: test.expected_output,
              actual: stdout.trim() || null,
              error: stderr || 'Failed to parse test results'
            })),
            compile_error: stderr.includes('SyntaxError') ? stderr : null,
            runtime_error: stderr || null
          });
        }
      });

      child.on('error', (err) => {
        clearTimeout(timeoutId);
        try {
          fs.unlinkSync(tempFile);
        } catch (e) {}

        resolve({
          results: [],
          compile_error: null,
          runtime_error: err.message
        });
      });

    } catch (err) {
      try {
        fs.unlinkSync(tempFile);
      } catch (e) {}

      resolve({
        results: [],
        compile_error: err instanceof SyntaxError ? err.message : null,
        runtime_error: err.message
      });
    }
  });
}

app.post('/execute', async (req, res) => {
  const { code, test_cases, entry_point, timeout_ms } = req.body;

  try {
    const result = await executeReactCode(
      code || '',
      test_cases || [],
      entry_point,
      timeout_ms || 10000
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
  res.json({ status: 'healthy', language: 'react' });
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, '0.0.0.0', () => {
  console.log(`React worker running on port ${PORT}`);
});
