'use client'

import { Level } from '@/types/roadmap'
import { cn } from '@/lib/utils'

interface LevelTabsProps {
  selectedLevel: Level
  onLevelChange: (level: Level) => void
}

const LEVELS: { value: Level; label: string; icon: string; description: string }[] = [
  {
    value: 'beginner',
    label: 'Beginner',
    icon: '🌱',
    description: 'Basic concepts and syntax',
  },
  {
    value: 'intermediate',
    label: 'Intermediate',
    icon: '🚀',
    description: 'Practical patterns and use cases',
  },
  {
    value: 'advanced',
    label: 'Advanced',
    icon: '⚡',
    description: 'Internals and optimization',
  },
]

export function LevelTabs({ selectedLevel, onLevelChange }: LevelTabsProps) {
  return (
    <div className="flex gap-2 overflow-x-auto pb-2">
      {LEVELS.map((level) => (
        <button
          key={level.value}
          onClick={() => onLevelChange(level.value)}
          className={cn(
            'flex-1 min-w-[140px] px-4 py-3 rounded-lg border transition-all',
            'hover:border-primary-500/50',
            selectedLevel === level.value
              ? 'bg-primary-600 border-primary-500 text-white'
              : 'bg-gray-800 border-gray-700 text-gray-300'
          )}
        >
          <div className="flex items-center justify-center gap-2 mb-1">
            <span className="text-lg">{level.icon}</span>
            <span className="font-semibold">{level.label}</span>
          </div>
          <div className="text-xs opacity-75">{level.description}</div>
        </button>
      ))}
    </div>
  )
}
