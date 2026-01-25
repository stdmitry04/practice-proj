'use client'

import { useEffect, useState } from 'react'
import { api } from '@/lib/api'
import { Topic } from '@/types'
import { usePracticeStore } from '@/stores/practiceStore'
import { Select } from '@/components/ui/Select'

export function TopicSelector() {
  const [topics, setTopics] = useState<Topic[]>([])
  const { selectedLanguage, selectedTopic, setSelectedTopic, setCurrentExercise } = usePracticeStore()

  useEffect(() => {
    if (selectedLanguage) {
      api.getTopics(selectedLanguage.id).then(setTopics).catch(console.error)
    } else {
      setTopics([])
    }
  }, [selectedLanguage])

  const handleChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const topic = topics.find((t) => t.id === e.target.value)
    if (topic) {
      setSelectedTopic(topic)
      setCurrentExercise(null)
    }
  }

  const options = topics.map((topic) => ({
    value: topic.id,
    label: `${topic.name} (${topic.difficulty})`,
  }))

  return (
    <Select
      value={selectedTopic?.id || ''}
      onChange={handleChange}
      options={options}
      placeholder="Select Topic"
      disabled={!selectedLanguage}
      className="w-64"
    />
  )
}
