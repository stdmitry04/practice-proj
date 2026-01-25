import { create } from 'zustand'
import { Language, Topic, Exercise, SubmitResult } from '@/types'

interface PracticeState {
  selectedLanguage: Language | null
  selectedTopic: Topic | null
  currentExercise: Exercise | null
  code: string
  isLoading: boolean
  submitResults: SubmitResult | null
  showSolution: boolean

  setSelectedLanguage: (language: Language | null) => void
  setSelectedTopic: (topic: Topic | null) => void
  setCurrentExercise: (exercise: Exercise | null) => void
  setCode: (code: string) => void
  setLoading: (loading: boolean) => void
  setSubmitResults: (results: SubmitResult | null) => void
  setShowSolution: (show: boolean) => void
  reset: () => void
}

const initialState = {
  selectedLanguage: null,
  selectedTopic: null,
  currentExercise: null,
  code: '',
  isLoading: false,
  submitResults: null,
  showSolution: false,
}

export const usePracticeStore = create<PracticeState>((set) => ({
  ...initialState,

  setSelectedLanguage: (language) =>
    set({ selectedLanguage: language, selectedTopic: null, currentExercise: null }),

  setSelectedTopic: (topic) =>
    set({ selectedTopic: topic }),

  setCurrentExercise: (exercise) =>
    set({
      currentExercise: exercise,
      code: exercise?.template_code || '',
      submitResults: null,
      showSolution: false,
    }),

  setCode: (code) => set({ code }),

  setLoading: (isLoading) => set({ isLoading }),

  setSubmitResults: (submitResults) => set({ submitResults }),

  setShowSolution: (showSolution) => set({ showSolution }),

  reset: () => set(initialState),
}))
