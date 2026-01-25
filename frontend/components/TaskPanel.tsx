'use client'

import ReactMarkdown from 'react-markdown'
import { usePracticeStore } from '@/stores/practiceStore'
import { clsx } from 'clsx'

export function TaskPanel() {
  const { currentExercise, submitResults, showSolution, isLoading } = usePracticeStore()

  if (!currentExercise) {
    return (
      <div className="h-full flex items-center justify-center text-gray-500 p-8">
        <div className="text-center">
          <div className="text-4xl mb-4">📝</div>
          <p>Select a topic and generate an exercise to get started</p>
        </div>
      </div>
    )
  }

  const testCases = currentExercise.test_cases?.test_cases || []
  const visibleTests = testCases.filter((t: any) => !t.hidden)

  return (
    <div className="p-6 space-y-6">
      {/* Title */}
      <div>
        <h2 className="text-2xl font-bold text-gray-900">{currentExercise.title}</h2>
      </div>

      {/* Description */}
      <div className="prose prose-sm max-w-none">
        <ReactMarkdown>{currentExercise.description}</ReactMarkdown>
      </div>

      {/* Hints */}
      {currentExercise.hints && currentExercise.hints.length > 0 && (
        <div className="bg-yellow-50 border border-yellow-200 rounded-lg p-4">
          <h3 className="font-semibold text-yellow-800 mb-2">Hints</h3>
          <ul className="list-disc list-inside space-y-1 text-yellow-700 text-sm">
            {currentExercise.hints.map((hint: string, idx: number) => (
              <li key={idx}>{hint}</li>
            ))}
          </ul>
        </div>
      )}

      {/* Test Cases Preview */}
      {visibleTests.length > 0 && (
        <div className="bg-gray-50 border border-gray-200 rounded-lg p-4">
          <h3 className="font-semibold text-gray-800 mb-3">Test Cases</h3>
          <div className="space-y-3">
            {visibleTests.map((test: any, idx: number) => (
              <div key={idx} className="bg-white rounded border border-gray-200 p-3 text-sm">
                <div className="font-medium text-gray-700 mb-1">{test.name}</div>
                <div className="grid grid-cols-2 gap-2 text-xs">
                  <div>
                    <span className="text-gray-500">Input:</span>
                    <pre className="mt-1 bg-gray-100 p-2 rounded overflow-x-auto">
                      {test.input}
                    </pre>
                  </div>
                  <div>
                    <span className="text-gray-500">Expected:</span>
                    <pre className="mt-1 bg-gray-100 p-2 rounded overflow-x-auto">
                      {test.expected_output}
                    </pre>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Submit Results */}
      {submitResults && (
        <div className={clsx(
          'border rounded-lg p-4',
          submitResults.passed
            ? 'bg-green-50 border-green-200'
            : 'bg-red-50 border-red-200'
        )}>
          <h3 className={clsx(
            'font-semibold mb-3',
            submitResults.passed ? 'text-green-800' : 'text-red-800'
          )}>
            {submitResults.passed ? '✅ All Tests Passed!' : '❌ Some Tests Failed'}
          </h3>

          {submitResults.compile_error && (
            <div className="bg-red-100 p-3 rounded mb-3 text-sm">
              <span className="font-medium">Compile Error:</span>
              <pre className="mt-1 whitespace-pre-wrap">{submitResults.compile_error}</pre>
            </div>
          )}

          {submitResults.runtime_error && (
            <div className="bg-red-100 p-3 rounded mb-3 text-sm">
              <span className="font-medium">Runtime Error:</span>
              <pre className="mt-1 whitespace-pre-wrap">{submitResults.runtime_error}</pre>
            </div>
          )}

          <div className="space-y-2">
            {submitResults.results.map((result, idx) => (
              <div
                key={idx}
                className={clsx(
                  'p-3 rounded text-sm',
                  result.passed ? 'bg-green-100' : 'bg-red-100'
                )}
              >
                <div className="flex items-center gap-2 mb-1">
                  <span>{result.passed ? '✓' : '✗'}</span>
                  <span className="font-medium">{result.name}</span>
                </div>
                {!result.passed && (
                  <div className="text-xs mt-2 space-y-1">
                    <div>
                      <span className="text-gray-600">Expected:</span>
                      <pre className="bg-white p-1 rounded mt-0.5">{result.expected}</pre>
                    </div>
                    <div>
                      <span className="text-gray-600">Actual:</span>
                      <pre className="bg-white p-1 rounded mt-0.5">{result.actual}</pre>
                    </div>
                    {result.error && (
                      <div>
                        <span className="text-gray-600">Error:</span>
                        <pre className="bg-white p-1 rounded mt-0.5 text-red-600">{result.error}</pre>
                      </div>
                    )}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Solution */}
      {showSolution && (
        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
          <h3 className="font-semibold text-blue-800 mb-3">Solution</h3>
          <pre className="bg-slate-800 text-slate-100 p-4 rounded-lg overflow-x-auto text-sm">
            {currentExercise.solution_code}
          </pre>
        </div>
      )}

      {isLoading && (
        <div className="fixed inset-0 bg-black bg-opacity-30 flex items-center justify-center z-50">
          <div className="bg-white rounded-lg p-6 shadow-xl">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600 mx-auto"></div>
            <p className="mt-3 text-gray-600">Processing...</p>
          </div>
        </div>
      )}
    </div>
  )
}
