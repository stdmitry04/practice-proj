import axios from 'axios'
import { Language, Topic, Exercise, SubmitResult } from '@/types'

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
}
