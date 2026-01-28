'use client'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { api } from '@/lib/api'
import { Language } from '@/types'
import { Card } from '@/components/ui/Card'

const LANGUAGE_ICONS: Record<string, string> = {
  react: '⚛️',
  javascript: '🟨',
  typescript: '🔷',
  python: '🐍',
  cpp: '⚙️',
}

const LANGUAGE_COLORS: Record<string, string> = {
  react: 'from-cyan-500 to-blue-500',
  javascript: 'from-yellow-400 to-orange-500',
  typescript: 'from-blue-500 to-blue-700',
  python: 'from-blue-500 to-green-500',
  cpp: 'from-blue-600 to-purple-600',
}

export default function HomePage() {
  const router = useRouter()
  const [languages, setLanguages] = useState<Language[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    async function fetchLanguages() {
      try {
        const data = await api.getLanguages()
        setLanguages(data)
      } catch (err) {
        setError('Failed to load languages')
        console.error(err)
      } finally {
        setLoading(false)
      }
    }

    fetchLanguages()
  }, [])

  const handleLanguageSelect = (language: Language) => {
    router.push(`/roadmap?lang=${language.slug}&langId=${language.id}`)
  }

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-600"></div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-red-500">{error}</div>
      </div>
    )
  }

  return (
    <main className="min-h-screen p-8 bg-gray-950">
      <div className="max-w-4xl mx-auto">
        <div className="text-center mb-12">
          <h1 className="text-4xl font-bold text-gray-100 mb-4">
            Code Practice Platform
          </h1>
          <p className="text-lg text-gray-400">
            Choose a language to start your learning journey
          </p>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {languages.map((language) => (
            <Card
              key={language.id}
              onClick={() => handleLanguageSelect(language)}
              className={`cursor-pointer transform transition-all duration-200 hover:scale-105 hover:shadow-xl`}
            >
              <div className={`absolute inset-0 bg-gradient-to-br ${LANGUAGE_COLORS[language.slug] || 'from-gray-400 to-gray-600'} opacity-20 rounded-xl`}></div>
              <div className="relative p-8">
                <div className="text-5xl mb-4">
                  {LANGUAGE_ICONS[language.slug] || '💻'}
                </div>
                <h2 className="text-2xl font-bold text-gray-100 mb-2">
                  {language.name}
                </h2>
                <p className="text-gray-400">
                  Practice {language.name} exercises with AI-generated tasks
                </p>
              </div>
            </Card>
          ))}
        </div>
      </div>
    </main>
  )
}
