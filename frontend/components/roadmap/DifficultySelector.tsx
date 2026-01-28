'use client'

import { Difficulty } from '@/types/roadmap'
import { clsx } from 'clsx'

interface DifficultySelectorProps {
  selected: Difficulty
  onChange: (difficulty: Difficulty) => void
}

const difficulties: { value: Difficulty; label: string; color: string }[] = [
  { value: 'easy', label: 'Easy', color: 'green' },
  { value: 'medium', label: 'Medium', color: 'yellow' },
  { value: 'hard', label: 'Hard', color: 'red' },
]

export function DifficultySelector({ selected, onChange }: DifficultySelectorProps) {
  return (
    <div className="flex gap-2">
      {difficulties.map(({ value, label, color }) => (
        <button
          key={value}
          onClick={() => onChange(value)}
          className={clsx(
            'px-4 py-2 rounded-lg font-medium transition-all',
            selected === value
              ? color === 'green'
                ? 'bg-green-600 text-white'
                : color === 'yellow'
                ? 'bg-yellow-600 text-white'
                : 'bg-red-600 text-white'
              : color === 'green'
              ? 'bg-green-900/50 text-green-400 hover:bg-green-900/70'
              : color === 'yellow'
              ? 'bg-yellow-900/50 text-yellow-400 hover:bg-yellow-900/70'
              : 'bg-red-900/50 text-red-400 hover:bg-red-900/70'
          )}
        >
          {label}
        </button>
      ))}
    </div>
  )
}
