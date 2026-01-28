'use client'

import { useEffect, useRef, useCallback } from 'react'
import Editor, { OnMount } from '@monaco-editor/react'
import ReactMarkdown from 'react-markdown'
import { clsx } from 'clsx'
import { useRoadmapStore } from '@/stores/roadmapStore'
import { api } from '@/lib/api'
import { Button } from '@/components/ui/Button'

export function ProblemModal() {
  const editorRef = useRef<any>(null)

  const {
    currentProblem,
    code,
    submitResult,
    showSolution,
    isSubmitting,
    isProblemModalOpen,
    setCode,
    setSubmitResult,
    setShowSolution,
    setSubmitting,
    closeProblem,
  } = useRoadmapStore()

  const handleEditorMount: OnMount = (editor) => {
    editorRef.current = editor
  }

  const handleEditorChange = (value: string | undefined) => {
    setCode(value || '')
  }

  const handleSubmit = async () => {
    if (!currentProblem) return

    setSubmitting(true)
    try {
      const result = await api.submitRoadmapProblem(currentProblem.id, code)
      setSubmitResult(result)
    } catch (err) {
      console.error('Failed to submit:', err)
    } finally {
      setSubmitting(false)
    }
  }

  const handleClose = useCallback(() => {
    closeProblem()
  }, [closeProblem])

  // Handle escape key
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape' && isProblemModalOpen) {
        handleClose()
      }
    }
    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [isProblemModalOpen, handleClose])

  if (!isProblemModalOpen || !currentProblem) return null

  const testCases = currentProblem.test_cases?.test_cases || []
  const visibleTests = testCases.filter((t) => !t.hidden)

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center">
      {/* Backdrop */}
      <div
        className="absolute inset-0 bg-black bg-opacity-50"
        onClick={handleClose}
      />

      {/* Modal */}
      <div className="relative w-[95vw] h-[90vh] bg-gray-900 rounded-lg shadow-2xl flex flex-col overflow-hidden border border-gray-700">
        {/* Header */}
        <div className="flex items-center justify-between px-6 py-4 border-b border-gray-700 bg-gray-800">
          <div>
            <h2 className="text-xl font-bold text-gray-100">{currentProblem.title}</h2>
            <div className="flex items-center gap-2 mt-1">
              <span
                className={clsx(
                  'px-2 py-0.5 text-xs rounded font-medium',
                  currentProblem.difficulty === 'easy'
                    ? 'bg-green-900/50 text-green-400'
                    : currentProblem.difficulty === 'medium'
                    ? 'bg-yellow-900/50 text-yellow-400'
                    : 'bg-red-900/50 text-red-400'
                )}
              >
                {currentProblem.difficulty.toUpperCase()}
              </span>
              <span
                className={clsx(
                  'px-2 py-0.5 text-xs rounded',
                  currentProblem.status === 'solved'
                    ? 'bg-green-900/50 text-green-400'
                    : currentProblem.status === 'attempted'
                    ? 'bg-yellow-900/50 text-yellow-400'
                    : 'bg-gray-700 text-gray-400'
                )}
              >
                {currentProblem.status}
              </span>
            </div>
          </div>
          <div className="flex items-center gap-3">
            <Button onClick={handleSubmit} disabled={isSubmitting} variant="success">
              {isSubmitting ? 'Running...' : 'Submit'}
            </Button>
            <Button
              onClick={() => setShowSolution(!showSolution)}
              variant="secondary"
            >
              {showSolution ? 'Hide Solution' : 'Show Solution'}
            </Button>
            <button
              onClick={handleClose}
              className="p-2 text-gray-400 hover:text-gray-200"
            >
              <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>

        {/* Content */}
        <div className="flex-1 flex overflow-hidden">
          {/* Left Panel - Description */}
          <div className="w-2/5 border-r border-gray-700 overflow-y-auto p-6 space-y-4 bg-gray-900">
            {/* Solution at top when shown */}
            {showSolution && (
              <div className="bg-blue-900/30 border border-blue-700 rounded-lg p-4">
                <h3 className="font-semibold text-blue-400 mb-3">Solution</h3>
                <pre className="bg-slate-800 text-slate-100 p-4 rounded-lg overflow-x-auto text-sm">
                  {currentProblem.solution_code}
                </pre>
              </div>
            )}

            {/* Description */}
            <div className="prose prose-sm prose-invert max-w-none">
              <ReactMarkdown>{currentProblem.description}</ReactMarkdown>
            </div>

            {/* Hints */}
            {currentProblem.hints && currentProblem.hints.length > 0 && (
              <div className="bg-yellow-900/30 border border-yellow-700 rounded-lg p-4">
                <h3 className="font-semibold text-yellow-400 mb-2">Hints</h3>
                <ul className="list-disc list-inside space-y-1 text-yellow-400 text-sm">
                  {currentProblem.hints.map((hint, idx) => (
                    <li key={idx}>{hint}</li>
                  ))}
                </ul>
              </div>
            )}

            {/* Test Cases */}
            {visibleTests.length > 0 && (
              <div className="bg-gray-800 border border-gray-700 rounded-lg p-4">
                <h3 className="font-semibold text-gray-100 mb-3">Test Cases</h3>
                <div className="space-y-3">
                  {visibleTests.map((test, idx) => (
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
            )}

            {/* Submit Results */}
            {submitResult && (
              <div
                className={clsx(
                  'border rounded-lg p-4',
                  submitResult.passed
                    ? 'bg-green-900/30 border-green-700'
                    : 'bg-red-900/30 border-red-700'
                )}
              >
                <h3
                  className={clsx(
                    'font-semibold mb-3',
                    submitResult.passed ? 'text-green-400' : 'text-red-400'
                  )}
                >
                  {submitResult.passed ? '✅ All Tests Passed!' : '❌ Some Tests Failed'}
                </h3>

                {submitResult.compile_error && (
                  <div className="bg-red-900/50 p-3 rounded mb-3 text-sm text-red-300">
                    <span className="font-medium">Compile Error:</span>
                    <pre className="mt-1 whitespace-pre-wrap">{submitResult.compile_error}</pre>
                  </div>
                )}

                {submitResult.runtime_error && (
                  <div className="bg-red-900/50 p-3 rounded mb-3 text-sm text-red-300">
                    <span className="font-medium">Runtime Error:</span>
                    <pre className="mt-1 whitespace-pre-wrap">{submitResult.runtime_error}</pre>
                  </div>
                )}

                <div className="space-y-2">
                  {submitResult.results.map((result, idx) => (
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
                              <pre className="bg-gray-800 p-1 rounded mt-0.5 text-red-400">
                                {result.error}
                              </pre>
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Right Panel - Editor */}
          <div className="w-3/5 flex flex-col">
            <div className="bg-slate-800 px-4 py-2 text-sm text-slate-300 flex items-center justify-between">
              <span>Python Editor</span>
              <span className="text-xs text-slate-500">
                Press Ctrl+S to format (if supported)
              </span>
            </div>
            <div className="flex-1">
              <Editor
                height="100%"
                language="python"
                value={code}
                onChange={handleEditorChange}
                onMount={handleEditorMount}
                theme="vs-dark"
                options={{
                  fontSize: 14,
                  fontFamily: 'JetBrains Mono, Menlo, Monaco, monospace',
                  minimap: { enabled: false },
                  scrollBeyondLastLine: false,
                  lineNumbers: 'on',
                  renderLineHighlight: 'all',
                  automaticLayout: true,
                  tabSize: 4,
                  wordWrap: 'on',
                  padding: { top: 16, bottom: 16 },
                }}
              />
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}
