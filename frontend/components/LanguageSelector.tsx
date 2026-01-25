'use client'

import { useEffect, useState } from 'react'
import { useRouter } from 'next/navigation'
import { api } from '@/lib/api'
import { Language } from '@/types'
import { usePracticeStore } from '@/stores/practiceStore'
import { Select } from '@/components/ui/Select'

export function LanguageSelector() {
  const router = useRouter()
  const [languages, setLanguages] = useState<Language[]>([])
  const { selectedLanguage, setSelectedLanguage, setSelectedTopic, setCurrentExercise } = usePracticeStore()

  useEffect(() => {
    api.getLanguages().then(setLanguages).catch(console.error)
  }, [])

  const handleChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const lang = languages.find((l) => l.id === e.target.value)
    if (lang) {
      setSelectedLanguage(lang)
      setSelectedTopic(null)
      setCurrentExercise(null)
      router.push(`/practice?lang=${lang.slug}&langId=${lang.id}`)
    }
  }

  const options = languages.map((lang) => ({
    value: lang.id,
    label: lang.name,
  }))

  return (
    <Select
      value={selectedLanguage?.id || ''}
      onChange={handleChange}
      options={options}
      placeholder="Select Language"
      className="w-40"
    />
  )
}
