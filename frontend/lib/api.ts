import axios from 'axios'
import { Language, Topic, Exercise, SubmitResult } from '@/types'
import {
  RoadmapNodeWithProgress,
  RoadmapProblem,
  RoadmapProblemSummary,
  Difficulty,
  Level,
  NodeProgress,
  SubmitResult as RoadmapSubmitResult,
} from '@/types/roadmap'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api'

const client = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000,
})

export const api = {
  async getLanguages(): Promise<Language[]> {
    const response = await client.get('/languages')
    return response.data
  },

  async getLanguage(id: string): Promise<Language> {
    const response = await client.get(`/languages/${id}`)
    return response.data
  },

  async getTopics(languageId: string): Promise<Topic[]> {
    const response = await client.get(`/languages/${languageId}/topics`)
    return response.data
  },

  async getTopic(topicId: string): Promise<Topic> {
    const response = await client.get(`/topics/${topicId}`)
    return response.data
  },

  async generateExercise(topicId: string): Promise<Exercise> {
    const response = await client.post('/exercises/generate', {
      topic_id: topicId,
    }, {
      timeout: 120000, // 2 minutes for AI generation
    })
    return response.data
  },

  async getExercise(exerciseId: string): Promise<Exercise> {
    const response = await client.get(`/exercises/${exerciseId}`)
    return response.data
  },

  async submitCode(exerciseId: string, code: string): Promise<SubmitResult> {
    const response = await client.post(`/exercises/${exerciseId}/submit`, {
      code,
    })
    return response.data
  },

  // Roadmap API
  async getLanguageRoadmap(languageId: string): Promise<RoadmapNodeWithProgress[]> {
    const response = await client.get(`/roadmap/languages/${languageId}/roadmap`)
    return response.data
  },

  async getRoadmapNode(nodeId: string): Promise<RoadmapNodeWithProgress> {
    const response = await client.get(`/roadmap/nodes/${nodeId}`)
    return response.data
  },

  async getNodeProblems(nodeId: string): Promise<RoadmapProblemSummary[]> {
    const response = await client.get(`/roadmap/nodes/${nodeId}/problems`)
    return response.data
  },

  async generateProblem(nodeId: string, difficulty: Difficulty, level: Level): Promise<RoadmapProblem> {
    const response = await client.post(`/roadmap/nodes/${nodeId}/generate`, {
      difficulty,
      level,
    }, {
      timeout: 120000, // 2 minutes for AI generation
    })
    return response.data
  },

  async generateModuleTest(nodeId: string): Promise<RoadmapProblem> {
    const response = await client.post(`/roadmap/nodes/${nodeId}/generate-module-test`, {}, {
      timeout: 120000, // 2 minutes for AI generation
    })
    return response.data
  },

  async getProblem(problemId: string): Promise<RoadmapProblem> {
    const response = await client.get(`/roadmap/problems/${problemId}`)
    return response.data
  },

  async deleteProblem(problemId: string): Promise<void> {
    await client.delete(`/roadmap/problems/${problemId}`)
  },

  async submitRoadmapProblem(problemId: string, code: string): Promise<RoadmapSubmitResult> {
    const response = await client.post(`/roadmap/problems/${problemId}/submit`, {
      code,
    })
    return response.data
  },

  async getNodeProgress(nodeId: string): Promise<NodeProgress> {
    const response = await client.get(`/roadmap/nodes/${nodeId}/progress`)
    return response.data
  },

  async getModuleCompletions(languageId: string): Promise<any[]> {
    const response = await client.get(`/roadmap/languages/${languageId}/modules/completion`)
    return response.data
  },
}
