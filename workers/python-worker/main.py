import subprocess
import tempfile
import os
import json
import resource
from flask import Flask, request, jsonify

app = Flask(__name__)

MAX_MEMORY_MB = 128
MAX_TIME_SECONDS = 10


def set_limits():
    """Set resource limits for subprocess"""
    resource.setrlimit(resource.RLIMIT_AS, (MAX_MEMORY_MB * 1024 * 1024, MAX_MEMORY_MB * 1024 * 1024))
    resource.setrlimit(resource.RLIMIT_CPU, (MAX_TIME_SECONDS, MAX_TIME_SECONDS))


def execute_python_code(code: str, test_cases: list, entry_point: str = None, timeout_ms: int = 5000) -> dict:
    """Execute Python code and run test cases"""
    results = []
    compile_error = None
    runtime_error = None

    timeout_seconds = timeout_ms / 1000

    for test in test_cases:
        test_name = test.get("name", "test")
        test_input = test.get("input", "")
        expected_output = test.get("expected_output", "")

        # Build test code
        if entry_point:
            # Function-based test
            test_code = f'''{code}

# Test execution
import json
args = json.loads('{json.dumps(test_input)}')
if isinstance(args, list):
    result = {entry_point}(*args)
else:
    result = {entry_point}(args)
print(result)
'''
        else:
            # stdin-based test
            test_code = code

        try:
            with tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False) as f:
                f.write(test_code)
                temp_file = f.name

            try:
                process = subprocess.run(
                    ['python', temp_file],
                    input=test_input if not entry_point else None,
                    capture_output=True,
                    text=True,
                    timeout=timeout_seconds,
                    preexec_fn=set_limits
                )

                actual_output = process.stdout.strip()
                stderr = process.stderr.strip()

                if process.returncode != 0:
                    results.append({
                        "name": test_name,
                        "passed": False,
                        "expected": expected_output,
                        "actual": actual_output,
                        "error": stderr or f"Exit code: {process.returncode}"
                    })
                else:
                    passed = actual_output == expected_output.strip()
                    results.append({
                        "name": test_name,
                        "passed": passed,
                        "expected": expected_output,
                        "actual": actual_output,
                        "error": None
                    })

            except subprocess.TimeoutExpired:
                results.append({
                    "name": test_name,
                    "passed": False,
                    "expected": expected_output,
                    "actual": None,
                    "error": "Execution timed out"
                })

            finally:
                os.unlink(temp_file)

        except SyntaxError as e:
            compile_error = str(e)
            break
        except Exception as e:
            runtime_error = str(e)
            results.append({
                "name": test_name,
                "passed": False,
                "expected": expected_output,
                "actual": None,
                "error": str(e)
            })

    return {
        "results": results,
        "compile_error": compile_error,
        "runtime_error": runtime_error
    }


@app.route('/execute', methods=['POST'])
def execute():
    data = request.json

    code = data.get('code', '')
    test_cases = data.get('test_cases', [])
    entry_point = data.get('entry_point')
    timeout_ms = data.get('timeout_ms', 5000)

    result = execute_python_code(code, test_cases, entry_point, timeout_ms)
    return jsonify(result)


@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy", "language": "python"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
