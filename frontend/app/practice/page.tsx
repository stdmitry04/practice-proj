'use client'

import { useEffect, Suspense } from 'react'
import { useSearchParams, useRouter } from 'next/navigation'
import { usePracticeStore } from '@/stores/practiceStore'
import { LanguageSelector } from '@/components/LanguageSelector'
import { TopicSelector } from '@/components/TopicSelector'
import { TaskPanel } from '@/components/TaskPanel'
import { CodeEditor } from '@/components/CodeEditor'
import { Button } from '@/components/ui/Button'
import { api } from '@/lib/api'

function PracticeContent() {
  const searchParams = useSearchParams()
  const router = useRouter()

  const {
    selectedLanguage,
    selectedTopic,
    currentExercise,
    code,
    isLoading,
    submitResults,
    setSelectedLanguage,
    setSelectedTopic,
    setCurrentExercise,
    setCode,
    setLoading,
    setSubmitResults,
    showSolution,
    setShowSolution,
  } = usePracticeStore()

  useEffect(() => {
    const langId = searchParams.get('langId')
    if (langId && !selectedLanguage) {
      api.getLanguage(langId).then((lang) => {
        setSelectedLanguage(lang)
      }).catch(console.error)
    }
  }, [searchParams, selectedLanguage, setSelectedLanguage])

  const handleGenerateExercise = async () => {
    if (!selectedTopic) return

    setLoading(true)
    setSubmitResults(null)
    setShowSolution(false)

    try {
      const exercise = await api.generateExercise(selectedTopic.id)
      setCurrentExercise(exercise)
      setCode(exercise.template_code)
    } catch (err) {
      console.error('Failed to generate exercise:', err)
    } finally {
      setLoading(false)
    }
  }

  const handleSubmit = async () => {
    if (!currentExercise) return

    setLoading(true)

    try {
      const result = await api.submitCode(currentExercise.id, code)
      setSubmitResults(result)
    } catch (err) {
      console.error('Failed to submit code:', err)
    } finally {
      setLoading(false)
    }
  }

  const handleBackHome = () => {
    router.push('/')
  }

  return (
    <div className="min-h-screen flex flex-col">
      {/* Header */}
      <header className="bg-white border-b border-gray-200 px-4 py-3">
        <div className="flex items-center gap-4">
          <button
            onClick={handleBackHome}
            className="text-gray-600 hover:text-gray-900"
          >
            ← Back
          </button>

          <LanguageSelector />
          <TopicSelector />

          <Button
            onClick={handleGenerateExercise}
            disabled={!selectedTopic || isLoading}
            variant="primary"
          >
            {isLoading ? 'Generating...' : 'Generate Exercise'}
          </Button>

          <div className="flex-1" />

          {currentExercise && (
            <>
              <Button
                onClick={handleSubmit}
                disabled={isLoading}
                variant="success"
              >
                {isLoading ? 'Running...' : 'Submit'}
              </Button>

              <Button
                onClick={() => setShowSolution(!showSolution)}
                variant="secondary"
              >
                {showSolution ? 'Hide Solution' : 'Show Solution'}
              </Button>
            </>
          )}
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 flex overflow-hidden">
        {/* Left Panel - Task */}
        <div className="w-2/5 border-r border-gray-200 overflow-auto bg-white">
          <TaskPanel />
        </div>

        {/* Right Panel - Editor */}
        <div className="w-3/5 flex flex-col overflow-hidden">
          <CodeEditor />
        </div>
      </main>
    </div>
  )
}

export default function PracticePage() {
  return (
    <Suspense fallback={
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    }>
      <PracticeContent />
    </Suspense>
  )
}
