'use client'

import { RoadmapProblemSummary } from '@/types/roadmap'
import { clsx } from 'clsx'

interface ProblemCardProps {
  problem: RoadmapProblemSummary
  onClick: () => void
  onDelete: () => void
  isDeleting?: boolean
}

export function ProblemCard({ problem, onClick, onDelete, isDeleting }: ProblemCardProps) {
  const statusColors = {
    unsolved: 'bg-gray-700 text-gray-400',
    attempted: 'bg-yellow-900/50 text-yellow-400',
    solved: 'bg-green-900/50 text-green-400',
  }

  const difficultyColors = {
    easy: 'bg-green-500',
    medium: 'bg-yellow-500',
    hard: 'bg-red-500',
  }

  return (
    <div
      className={clsx(
        'p-4 border rounded-lg cursor-pointer transition-all hover:shadow-md',
        problem.status === 'solved'
          ? 'border-green-700 bg-green-900/30'
          : problem.status === 'attempted'
          ? 'border-yellow-700 bg-yellow-900/30'
          : 'border-gray-700 bg-gray-800'
      )}
    >
      <div className="flex items-start justify-between gap-3">
        <div className="flex-1 min-w-0" onClick={onClick}>
          <div className="flex items-center gap-2 mb-1">
            <span
              className={clsx(
                'w-2 h-2 rounded-full',
                difficultyColors[problem.difficulty]
              )}
            />
            <h4 className="font-medium text-gray-100 truncate">{problem.title}</h4>
          </div>
          <div className="flex items-center gap-2 text-xs">
            <span className={clsx('px-2 py-0.5 rounded', statusColors[problem.status])}>
              {problem.status.charAt(0).toUpperCase() + problem.status.slice(1)}
            </span>
            <span className="text-gray-500">
              {new Date(problem.created_at).toLocaleDateString()}
            </span>
          </div>
        </div>
        <button
          onClick={(e) => {
            e.stopPropagation()
            onDelete()
          }}
          disabled={isDeleting}
          className={clsx(
            'p-1 text-gray-500 hover:text-red-400 transition-colors',
            isDeleting && 'opacity-50 cursor-not-allowed'
          )}
          title="Delete problem"
        >
          <svg
            className="w-5 h-5"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"
            />
          </svg>
        </button>
      </div>
    </div>
  )
}
