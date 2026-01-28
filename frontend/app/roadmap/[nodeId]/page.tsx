'use client'

import { useEffect, useState } from 'react'
import { useParams, useRouter } from 'next/navigation'
import { useRoadmapStore } from '@/stores/roadmapStore'
import { DifficultySelector, ProblemCard, ProblemModal } from '@/components/roadmap'
import { Button } from '@/components/ui/Button'
import { api } from '@/lib/api'
import { RoadmapNodeWithProgress, RoadmapProblem } from '@/types/roadmap'

export default function NodeDetailPage() {
  const params = useParams()
  const router = useRouter()
  const nodeId = params.nodeId as string

  const [node, setNode] = useState<RoadmapNodeWithProgress | null>(null)
  const [deletingProblemId, setDeletingProblemId] = useState<string | null>(null)

  const {
    problems,
    selectedDifficulty,
    isLoadingProblems,
    isGenerating,
    setProblems,
    setSelectedDifficulty,
    setLoadingProblems,
    setGenerating,
    openProblem,
    removeProblem,
  } = useRoadmapStore()

  // Load node details
  useEffect(() => {
    if (!nodeId) return

    api.getRoadmapNode(nodeId).then(setNode).catch(console.error)
  }, [nodeId])

  // Load problems when node changes
  useEffect(() => {
    if (!nodeId) return

    setLoadingProblems(true)
    api
      .getNodeProblems(nodeId)
      .then(setProblems)
      .catch(console.error)
      .finally(() => setLoadingProblems(false))
  }, [nodeId, setProblems, setLoadingProblems])

  const handleGenerateProblem = async () => {
    if (!nodeId) return

    setGenerating(true)
    try {
      const newProblem = await api.generateProblem(nodeId, selectedDifficulty)
      // Refresh the problems list
      const updatedProblems = await api.getNodeProblems(nodeId)
      setProblems(updatedProblems)
    } catch (err) {
      console.error('Failed to generate problem:', err)
    } finally {
      setGenerating(false)
    }
  }

  const handleProblemClick = async (problemId: string) => {
    try {
      const problem = await api.getProblem(problemId)
      openProblem(problem)
    } catch (err) {
      console.error('Failed to load problem:', err)
    }
  }

  const handleDeleteProblem = async (problemId: string) => {
    if (!confirm('Are you sure you want to delete this problem?')) return

    setDeletingProblemId(problemId)
    try {
      await api.deleteProblem(problemId)
      removeProblem(problemId)
    } catch (err) {
      console.error('Failed to delete problem:', err)
    } finally {
      setDeletingProblemId(null)
    }
  }

  const handleBack = () => {
    router.push('/roadmap')
  }

  // Filter problems by selected difficulty
  const filteredProblems = problems.filter((p) => p.difficulty === selectedDifficulty)

  return (
    <div className="min-h-screen flex flex-col bg-gray-950">
      {/* Header */}
      <header className="bg-gray-900 border-b border-gray-700 px-4 py-3">
        <div className="flex items-center gap-4">
          <button onClick={handleBack} className="text-gray-400 hover:text-gray-100">
            ← Back to Roadmap
          </button>

          <div className="flex-1">
            {node && (
              <div>
                <h1 className="text-xl font-bold text-gray-100">{node.name}</h1>
                {node.description && (
                  <p className="text-sm text-gray-400">{node.description}</p>
                )}
              </div>
            )}
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1 p-6">
        <div className="max-w-4xl mx-auto">
          {/* Difficulty selector and generate button */}
          <div className="bg-gray-900 rounded-lg border border-gray-700 p-6 mb-6">
            <div className="flex items-center justify-between">
              <div>
                <h2 className="text-lg font-semibold text-gray-100 mb-3">
                  Select Difficulty
                </h2>
                <DifficultySelector
                  selected={selectedDifficulty}
                  onChange={setSelectedDifficulty}
                />
              </div>

              <Button
                onClick={handleGenerateProblem}
                disabled={isGenerating}
                variant="primary"
                className="ml-6"
              >
                {isGenerating ? (
                  <>
                    <span className="animate-spin mr-2">⏳</span>
                    Generating...
                  </>
                ) : (
                  'Generate Problem'
                )}
              </Button>
            </div>

            {node?.concept_keywords && node.concept_keywords.length > 0 && (
              <div className="mt-4 pt-4 border-t border-gray-700">
                <span className="text-sm text-gray-400">Concepts covered: </span>
                <div className="flex flex-wrap gap-2 mt-2">
                  {node.concept_keywords.map((keyword, idx) => (
                    <span
                      key={idx}
                      className="px-2 py-1 bg-gray-800 text-gray-300 text-xs rounded"
                    >
                      {keyword}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </div>

          {/* Problems list */}
          <div className="bg-gray-900 rounded-lg border border-gray-700 p-6">
            <h2 className="text-lg font-semibold text-gray-100 mb-4">
              {selectedDifficulty.charAt(0).toUpperCase() + selectedDifficulty.slice(1)} Problems
              <span className="text-sm font-normal text-gray-400 ml-2">
                ({filteredProblems.length} total)
              </span>
            </h2>

            {isLoadingProblems ? (
              <div className="text-center py-8">
                <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-primary-500 mx-auto"></div>
                <p className="mt-3 text-gray-400">Loading problems...</p>
              </div>
            ) : filteredProblems.length === 0 ? (
              <div className="text-center py-8 text-gray-400">
                <div className="text-3xl mb-2">📝</div>
                <p>No {selectedDifficulty} problems yet.</p>
                <p className="text-sm mt-1">
                  Click &quot;Generate Problem&quot; to create one!
                </p>
              </div>
            ) : (
              <div className="space-y-3">
                {filteredProblems.map((problem) => (
                  <ProblemCard
                    key={problem.id}
                    problem={problem}
                    onClick={() => handleProblemClick(problem.id)}
                    onDelete={() => handleDeleteProblem(problem.id)}
                    isDeleting={deletingProblemId === problem.id}
                  />
                ))}
              </div>
            )}
          </div>

          {/* Progress summary */}
          {node && (
            <div className="mt-6 bg-gray-900 rounded-lg border border-gray-700 p-6">
              <h2 className="text-lg font-semibold text-gray-100 mb-4">
                Progress Summary
              </h2>
              <div className="grid grid-cols-3 gap-4">
                <div className="text-center p-4 bg-green-900/30 border border-green-700 rounded-lg">
                  <div className="text-2xl font-bold text-green-400">
                    {node.easy_solved}/{node.easy_count}
                  </div>
                  <div className="text-sm text-green-400">Easy</div>
                </div>
                <div className="text-center p-4 bg-yellow-900/30 border border-yellow-700 rounded-lg">
                  <div className="text-2xl font-bold text-yellow-400">
                    {node.medium_solved}/{node.medium_count}
                  </div>
                  <div className="text-sm text-yellow-400">Medium</div>
                </div>
                <div className="text-center p-4 bg-red-900/30 border border-red-700 rounded-lg">
                  <div className="text-2xl font-bold text-red-400">
                    {node.hard_solved}/{node.hard_count}
                  </div>
                  <div className="text-sm text-red-400">Hard</div>
                </div>
              </div>
            </div>
          )}
        </div>
      </main>

      {/* Problem Modal */}
      <ProblemModal />
    </div>
  )
}
