import { create } from 'zustand'
import {
  RoadmapNodeWithProgress,
  RoadmapProblem,
  RoadmapProblemSummary,
  Difficulty,
  SubmitResult,
} from '@/types/roadmap'

interface RoadmapState {
  // Nodes
  nodes: RoadmapNodeWithProgress[]
  selectedNode: RoadmapNodeWithProgress | null

  // Problems
  problems: RoadmapProblemSummary[]
  currentProblem: RoadmapProblem | null
  selectedDifficulty: Difficulty

  // Code editor state
  code: string
  submitResult: SubmitResult | null
  showSolution: boolean

  // Loading states
  isLoadingNodes: boolean
  isLoadingProblems: boolean
  isGenerating: boolean
  isSubmitting: boolean

  // Modal state
  isProblemModalOpen: boolean

  // Actions
  setNodes: (nodes: RoadmapNodeWithProgress[]) => void
  setSelectedNode: (node: RoadmapNodeWithProgress | null) => void
  setProblems: (problems: RoadmapProblemSummary[]) => void
  setCurrentProblem: (problem: RoadmapProblem | null) => void
  setSelectedDifficulty: (difficulty: Difficulty) => void
  setCode: (code: string) => void
  setSubmitResult: (result: SubmitResult | null) => void
  setShowSolution: (show: boolean) => void
  setLoadingNodes: (loading: boolean) => void
  setLoadingProblems: (loading: boolean) => void
  setGenerating: (generating: boolean) => void
  setSubmitting: (submitting: boolean) => void
  setProblemModalOpen: (open: boolean) => void
  openProblem: (problem: RoadmapProblem) => void
  closeProblem: () => void
  updateNodeProgress: (nodeId: string, difficulty: Difficulty, solved: boolean) => void
  removeProblem: (problemId: string) => void
  reset: () => void
}

const initialState = {
  nodes: [],
  selectedNode: null,
  problems: [],
  currentProblem: null,
  selectedDifficulty: 'easy' as Difficulty,
  code: '',
  submitResult: null,
  showSolution: false,
  isLoadingNodes: false,
  isLoadingProblems: false,
  isGenerating: false,
  isSubmitting: false,
  isProblemModalOpen: false,
}

export const useRoadmapStore = create<RoadmapState>((set, get) => ({
  ...initialState,

  setNodes: (nodes) => set({ nodes }),

  setSelectedNode: (node) => set({ selectedNode: node, problems: [], currentProblem: null }),

  setProblems: (problems) => set({ problems }),

  setCurrentProblem: (problem) => set({
    currentProblem: problem,
    code: problem?.template_code || '',
    submitResult: null,
    showSolution: false,
  }),

  setSelectedDifficulty: (difficulty) => set({ selectedDifficulty: difficulty }),

  setCode: (code) => set({ code }),

  setSubmitResult: (result) => set({ submitResult: result }),

  setShowSolution: (show) => set({ showSolution: show }),

  setLoadingNodes: (loading) => set({ isLoadingNodes: loading }),

  setLoadingProblems: (loading) => set({ isLoadingProblems: loading }),

  setGenerating: (generating) => set({ isGenerating: generating }),

  setSubmitting: (submitting) => set({ isSubmitting: submitting }),

  setProblemModalOpen: (open) => set({ isProblemModalOpen: open }),

  openProblem: (problem) => set({
    currentProblem: problem,
    code: problem.template_code,
    submitResult: null,
    showSolution: false,
    isProblemModalOpen: true,
  }),

  closeProblem: () => set({
    currentProblem: null,
    code: '',
    submitResult: null,
    showSolution: false,
    isProblemModalOpen: false,
  }),

  updateNodeProgress: (nodeId, difficulty, solved) => {
    const { nodes } = get()
    const updatedNodes = nodes.map((node) => {
      if (node.id !== nodeId) return node

      const updates: Partial<RoadmapNodeWithProgress> = {}
      const countKey = `${difficulty}_count` as keyof RoadmapNodeWithProgress
      const solvedKey = `${difficulty}_solved` as keyof RoadmapNodeWithProgress

      if (solved) {
        updates[solvedKey] = (node[solvedKey] as number) + 1
      }
      updates[countKey] = (node[countKey] as number) + 1

      return { ...node, ...updates }
    })

    set({ nodes: updatedNodes })
  },

  removeProblem: (problemId) => {
    const { problems } = get()
    set({ problems: problems.filter((p) => p.id !== problemId) })
  },

  reset: () => set(initialState),
}))
