'use client'

import { memo } from 'react'
import { Handle, Position, NodeProps } from 'reactflow'
import { RoadmapNodeWithProgress, NodeTopic } from '@/types/roadmap'
import { clsx } from 'clsx'

// Topic color mapping for left border accent
const topicColors: Record<NodeTopic, string> = {
  fundamentals: 'border-l-blue-500',
  oop: 'border-l-purple-500',
  'data-structures': 'border-l-cyan-500',
  tooling: 'border-l-orange-500',
  web: 'border-l-emerald-500',
  database: 'border-l-amber-500',
  'data-science': 'border-l-pink-500',
  concurrency: 'border-l-red-500',
  typing: 'border-l-indigo-500',
}

function CustomNodeComponent({ data: node }: NodeProps<RoadmapNodeWithProgress>) {

  const hasProgress = node.easy_count > 0 || node.medium_count > 0 || node.hard_count > 0
  const isComplete =
    (node.easy_count === 0 || node.easy_solved === node.easy_count) &&
    (node.medium_count === 0 || node.medium_solved === node.medium_count) &&
    (node.hard_count === 0 || node.hard_solved === node.hard_count) &&
    hasProgress

  const topicBorderClass = node.topic ? topicColors[node.topic] : ''
  const isLocked = node.is_locked

  return (
    <div
      className={clsx(
        'px-4 py-3 rounded-lg border-2 cursor-pointer transition-all relative',
        'hover:shadow-lg hover:scale-105',
        'min-w-[180px] max-w-[220px]',
        isLocked && 'opacity-50 grayscale cursor-not-allowed pointer-events-none',
        isComplete
          ? 'bg-green-900/40 border-green-500'
          : hasProgress
          ? 'bg-blue-900/40 border-blue-500'
          : 'bg-gray-800 border-gray-600',
        // Topic left border accent (only when topic exists)
        node.topic && 'border-l-4',
        topicBorderClass
      )}
    >
      <Handle type="target" position={Position.Top} className="!bg-gray-500" />

      {/* Lock overlay */}
      {isLocked && (
        <div className="absolute inset-0 flex items-center justify-center">
          <div className="text-4xl">🔒</div>
        </div>
      )}

      <div className="text-center">
        <h3 className="font-semibold text-gray-100 text-sm mb-2">{node.name}</h3>

        {/* Difficulty circles with counters */}
        <div className="flex justify-center gap-3 mt-1">
          {/* Easy - Green */}
          <div className="flex flex-col items-center">
            <div
              className={clsx(
                'w-4 h-4 rounded-full border-2',
                node.easy_solved === node.easy_count && node.easy_count > 0
                  ? 'bg-green-500 border-green-400'
                  : 'bg-green-900/50 border-green-600'
              )}
            />
            <span className="text-[10px] text-gray-400 mt-0.5">
              {node.easy_solved}/{node.easy_count}
            </span>
          </div>
          {/* Medium - Yellow */}
          <div className="flex flex-col items-center">
            <div
              className={clsx(
                'w-4 h-4 rounded-full border-2',
                node.medium_solved === node.medium_count && node.medium_count > 0
                  ? 'bg-yellow-500 border-yellow-400'
                  : 'bg-yellow-900/50 border-yellow-600'
              )}
            />
            <span className="text-[10px] text-gray-400 mt-0.5">
              {node.medium_solved}/{node.medium_count}
            </span>
          </div>
          {/* Hard - Red */}
          <div className="flex flex-col items-center">
            <div
              className={clsx(
                'w-4 h-4 rounded-full border-2',
                node.hard_solved === node.hard_count && node.hard_count > 0
                  ? 'bg-red-500 border-red-400'
                  : 'bg-red-900/50 border-red-600'
              )}
            />
            <span className="text-[10px] text-gray-400 mt-0.5">
              {node.hard_solved}/{node.hard_count}
            </span>
          </div>
        </div>
      </div>

      <Handle type="source" position={Position.Bottom} className="!bg-gray-500" />
    </div>
  )
}

export const CustomNode = memo(CustomNodeComponent)
