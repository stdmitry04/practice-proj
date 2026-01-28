'use client'

import ReactMarkdown from 'react-markdown'
import { usePracticeStore } from '@/stores/practiceStore'
import { clsx } from 'clsx'

export function TaskPanel() {
  const { currentExercise, submitResults, showSolution, isLoading } = usePracticeStore()

  if (!currentExercise) {
    return (
      <div className="h-full flex items-center justify-center text-gray-400 p-8">
        <div className="text-center">
          <div className="text-4xl mb-4">📝</div>
          <p>Select a topic and generate an exercise to get started</p>
        </div>
      </div>
    )
  }

  const testCases = currentExercise.test_cases?.test_cases || []
  const visibleTests = testCases.filter((t: any) => !t.hidden)

  // Solution section - extracted for conditional positioning
  const solutionSection = showSolution && (
    <div className="bg-blue-900/30 border border-blue-700 rounded-lg p-4">
      <h3 className="font-semibold text-blue-400 mb-3">Solution</h3>
      <pre className="bg-slate-800 text-slate-100 p-4 rounded-lg overflow-x-auto text-sm">
        {currentExercise.solution_code}
      </pre>
    </div>
  )

  // Title section
  const titleSection = (
    <div>
      <h2 className="text-2xl font-bold text-gray-100">{currentExercise.title}</h2>
    </div>
  )

  // Description section
  const descriptionSection = (
    <div className="prose prose-sm max-w-none">
      <ReactMarkdown>{currentExercise.description}</ReactMarkdown>
    </div>
  )

  // Hints section
  const hintsSection = currentExercise.hints && currentExercise.hints.length > 0 && (
    <div className="bg-yellow-900/30 border border-yellow-700 rounded-lg p-4">
      <h3 className="font-semibold text-yellow-400 mb-2">Hints</h3>
      <ul className="list-disc list-inside space-y-1 text-yellow-400 text-sm">
        {currentExercise.hints.map((hint: string, idx: number) => (
          <li key={idx}>{hint}</li>
        ))}
      </ul>
    </div>
  )

  // Test cases section
  const testCasesSection = visibleTests.length > 0 && (
    <div className="bg-gray-800 border border-gray-700 rounded-lg p-4">
      <h3 className="font-semibold text-gray-100 mb-3">Test Cases</h3>
      <div className="space-y-3">
        {visibleTests.map((test: any, idx: number) => (
          <div key={idx} className="bg-gray-900 rounded border border-gray-700 p-3 text-sm">
            <div className="font-medium text-gray-300 mb-1">{test.name}</div>
            <div className="grid grid-cols-2 gap-2 text-xs">
              <div>
                <span className="text-gray-400">Input:</span>
                <pre className="mt-1 bg-gray-800 text-gray-300 p-2 rounded overflow-x-auto">
                  {test.input}
                </pre>
              </div>
              <div>
                <span className="text-gray-400">Expected:</span>
                <pre className="mt-1 bg-gray-800 text-gray-300 p-2 rounded overflow-x-auto">
                  {test.expected_output}
                </pre>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )

  // Submit results section
  const submitResultsSection = submitResults && (
    <div className={clsx(
      'border rounded-lg p-4',
      submitResults.passed
        ? 'bg-green-900/30 border-green-700'
        : 'bg-red-900/30 border-red-700'
    )}>
      <h3 className={clsx(
        'font-semibold mb-3',
        submitResults.passed ? 'text-green-400' : 'text-red-400'
      )}>
        {submitResults.passed ? '✅ All Tests Passed!' : '❌ Some Tests Failed'}
      </h3>

      {submitResults.compile_error && (
        <div className="bg-red-900/50 p-3 rounded mb-3 text-sm text-red-300">
          <span className="font-medium">Compile Error:</span>
          <pre className="mt-1 whitespace-pre-wrap">{submitResults.compile_error}</pre>
        </div>
      )}

      {submitResults.runtime_error && (
        <div className="bg-red-900/50 p-3 rounded mb-3 text-sm text-red-300">
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
              result.passed ? 'bg-green-900/50 text-green-300' : 'bg-red-900/50 text-red-300'
            )}
          >
            <div className="flex items-center gap-2 mb-1">
              <span>{result.passed ? '✓' : '✗'}</span>
              <span className="font-medium">{result.name}</span>
            </div>
            {!result.passed && (
              <div className="text-xs mt-2 space-y-1">
                <div>
                  <span className="text-gray-400">Expected:</span>
                  <pre className="bg-gray-800 text-gray-300 p-1 rounded mt-0.5">{result.expected}</pre>
                </div>
                <div>
                  <span className="text-gray-400">Actual:</span>
                  <pre className="bg-gray-800 text-gray-300 p-1 rounded mt-0.5">{result.actual}</pre>
                </div>
                {result.error && (
                  <div>
                    <span className="text-gray-400">Error:</span>
                    <pre className="bg-gray-800 p-1 rounded mt-0.5 text-red-400">{result.error}</pre>
                  </div>
                )}
              </div>
            )}
          </div>
        ))}
      </div>
    </div>
  )

  return (
    <div className="p-6 space-y-6">
      {/* When solution is shown, it appears at the top */}
      {showSolution && solutionSection}
      {titleSection}
      {descriptionSection}
      {hintsSection}
      {testCasesSection}
      {submitResultsSection}

      {isLoading && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
          <div className="bg-gray-800 rounded-lg p-6 shadow-xl border border-gray-700">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-500 mx-auto"></div>
            <p className="mt-3 text-gray-300">Processing...</p>
          </div>
        </div>
      )}
    </div>
  )
}
