'use client'

import { useEffect, useState } from 'react'
import { useRouter, useSearchParams } from 'next/navigation'
import { useRoadmapStore } from '@/stores/roadmapStore'
import { RoadmapCanvas } from '@/components/roadmap'
import { api } from '@/lib/api'
import { Language } from '@/types'
import { RoadmapNodeWithProgress } from '@/types/roadmap'

export default function RoadmapPage() {
  const router = useRouter()
  const searchParams = useSearchParams()
  const [languages, setLanguages] = useState<Language[]>([])
  const [selectedLanguage, setSelectedLanguage] = useState<Language | null>(null)

  const { nodes, isLoadingNodes, setNodes, setLoadingNodes, setSelectedNode } = useRoadmapStore()

  // Load languages on mount and handle query params
  useEffect(() => {
    api.getLanguages().then((langs) => {
      setLanguages(langs)

      // Check for lang/langId query params first
      const langSlug = searchParams.get('lang')
      const langId = searchParams.get('langId')

      if (langId) {
        const langFromId = langs.find((l) => l.id === langId)
        if (langFromId) {
          setSelectedLanguage(langFromId)
          return
        }
      }

      if (langSlug) {
        const langFromSlug = langs.find((l) => l.slug === langSlug)
        if (langFromSlug) {
          setSelectedLanguage(langFromSlug)
          return
        }
      }

      // Fall back to Python if available, otherwise first language
      const python = langs.find((l) => l.slug === 'python')
      if (python) {
        setSelectedLanguage(python)
      } else if (langs.length > 0) {
        setSelectedLanguage(langs[0])
      }
    })
  }, [searchParams])

  // Load roadmap when language changes
  useEffect(() => {
    if (!selectedLanguage) return

    console.log('[RoadmapPage] Loading roadmap for language:', selectedLanguage)
    setLoadingNodes(true)
    api
      .getLanguageRoadmap(selectedLanguage.id)
      .then((roadmapNodes) => {
        console.log('[RoadmapPage] Received roadmap nodes from API:', roadmapNodes)
        setNodes(roadmapNodes)
      })
      .catch((err) => {
        console.error('[RoadmapPage] Error loading roadmap:', err)
      })
      .finally(() => setLoadingNodes(false))
  }, [selectedLanguage, setNodes, setLoadingNodes])

  const handleNodeClick = (node: RoadmapNodeWithProgress) => {
    setSelectedNode(node)
    router.push(`/roadmap/${node.id}`)
  }

  const handleBackHome = () => {
    router.push('/')
  }

  return (
    <div className="min-h-screen flex flex-col bg-gray-950">
      {/* Header */}
      <header className="bg-gray-900 border-b border-gray-700 px-4 py-3">
        <div className="flex items-center gap-4">
          <button
            onClick={handleBackHome}
            className="text-gray-400 hover:text-gray-100"
          >
            ← Back
          </button>

          <h1 className="text-xl font-bold text-gray-100">Learning Roadmap</h1>

          <select
            value={selectedLanguage?.id || ''}
            onChange={(e) => {
              const lang = languages.find((l) => l.id === e.target.value)
              if (lang) setSelectedLanguage(lang)
            }}
            className="px-3 py-2 border border-gray-700 bg-gray-800 text-gray-100 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-primary-500"
          >
            {languages.map((lang) => (
              <option key={lang.id} value={lang.id}>
                {lang.name}
              </option>
            ))}
          </select>

          <div className="flex-1" />

          <div className="text-sm text-gray-400">
            Click on a concept to practice
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="flex-1" style={{ height: 'calc(100vh - 64px)' }}>
        {isLoadingNodes ? (
          <div className="h-full flex items-center justify-center">
            <div className="text-center">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500 mx-auto"></div>
              <p className="mt-4 text-gray-400">Loading roadmap...</p>
            </div>
          </div>
        ) : nodes.length === 0 ? (
          <div className="h-full flex items-center justify-center">
            <div className="text-center text-gray-400">
              <div className="text-4xl mb-4">🗺️</div>
              <p>No roadmap available for this language yet.</p>
              <p className="text-sm mt-2">Run the seed script to populate the roadmap.</p>
            </div>
          </div>
        ) : (
          <RoadmapCanvas nodes={nodes} onNodeClick={handleNodeClick} />
        )}
      </main>
    </div>
  )
}
