import React from 'react'
import { Handle, Position, NodeProps } from 'reactflow'
import { RoadmapNodeWithProgress, NodeTopic } from '@/types/roadmap'

interface HexagonalNodeData extends RoadmapNodeWithProgress {
  onClick: (nodeId: string) => void
}

// Topic colors for hexagonal nodes
const topicColors: Record<NodeTopic, { bg: string; border: string; text: string; bgComplete: string; borderComplete: string }> = {
  fundamentals: { bg: 'bg-blue-900/40', border: 'border-blue-500', text: 'text-blue-200', bgComplete: 'bg-blue-700/60', borderComplete: 'border-blue-300' },
  oop: { bg: 'bg-purple-900/40', border: 'border-purple-500', text: 'text-purple-200', bgComplete: 'bg-purple-700/60', borderComplete: 'border-purple-300' },
  'data-structures': { bg: 'bg-cyan-900/40', border: 'border-cyan-500', text: 'text-cyan-200', bgComplete: 'bg-cyan-700/60', borderComplete: 'border-cyan-300' },
  tooling: { bg: 'bg-orange-900/40', border: 'border-orange-500', text: 'text-orange-200', bgComplete: 'bg-orange-700/60', borderComplete: 'border-orange-300' },
  web: { bg: 'bg-emerald-900/40', border: 'border-emerald-500', text: 'text-emerald-200', bgComplete: 'bg-emerald-700/60', borderComplete: 'border-emerald-300' },
  database: { bg: 'bg-amber-900/40', border: 'border-amber-500', text: 'text-amber-200', bgComplete: 'bg-amber-700/60', borderComplete: 'border-amber-300' },
  'data-science': { bg: 'bg-pink-900/40', border: 'border-pink-500', text: 'text-pink-200', bgComplete: 'bg-pink-700/60', borderComplete: 'border-pink-300' },
  concurrency: { bg: 'bg-red-900/40', border: 'border-red-500', text: 'text-red-200', bgComplete: 'bg-red-700/60', borderComplete: 'border-red-300' },
  typing: { bg: 'bg-indigo-900/40', border: 'border-indigo-500', text: 'text-indigo-200', bgComplete: 'bg-indigo-700/60', borderComplete: 'border-indigo-300' },
}

export function HexagonalNode({ data }: NodeProps<HexagonalNodeData>) {
  const isComplete = data.hard_solved >= 1
  const onClick = () => data.onClick(data.id)

  const colors = data.topic ? topicColors[data.topic] : topicColors.fundamentals

  return (
    <div
      onClick={onClick}
      className="relative cursor-pointer transition-all hover:scale-105"
      style={{ width: '160px', height: '140px' }}
    >
      {/* Hexagonal shape using clip-path */}
      <div
        className={`
          w-full h-full flex flex-col items-center justify-center
          transition-all border-2
          ${isComplete ? colors.bgComplete : colors.bg}
          ${isComplete ? colors.borderComplete : colors.border}
        `}
        style={{
          clipPath:
            'polygon(50% 0%, 100% 25%, 100% 75%, 50% 100%, 0% 75%, 0% 25%)',
        }}
      >
        <div className="text-3xl mb-2">🎯</div>
        <div className={`text-xs font-semibold text-center px-2 ${colors.text}`}>
          Module Test
        </div>
        {/* Difficulty circles with counters */}
        <div className="flex justify-center gap-2 mt-1">
          {/* Easy - Green */}
          <div className="flex flex-col items-center">
            <div
              className={`w-3 h-3 rounded-full border ${
                data.easy_solved === data.easy_count && data.easy_count > 0
                  ? 'bg-green-500 border-green-400'
                  : 'bg-green-900/50 border-green-600'
              }`}
            />
            <span className="text-[8px] text-gray-300">
              {data.easy_solved}/{data.easy_count}
            </span>
          </div>
          {/* Medium - Yellow */}
          <div className="flex flex-col items-center">
            <div
              className={`w-3 h-3 rounded-full border ${
                data.medium_solved === data.medium_count && data.medium_count > 0
                  ? 'bg-yellow-500 border-yellow-400'
                  : 'bg-yellow-900/50 border-yellow-600'
              }`}
            />
            <span className="text-[8px] text-gray-300">
              {data.medium_solved}/{data.medium_count}
            </span>
          </div>
          {/* Hard - Red */}
          <div className="flex flex-col items-center">
            <div
              className={`w-3 h-3 rounded-full border ${
                data.hard_solved === data.hard_count && data.hard_count > 0
                  ? 'bg-red-500 border-red-400'
                  : 'bg-red-900/50 border-red-600'
              }`}
            />
            <span className="text-[8px] text-gray-300">
              {data.hard_solved}/{data.hard_count}
            </span>
          </div>
        </div>
      </div>

      {/* Node name below hexagon */}
      <div className="absolute -bottom-6 left-0 right-0 text-center">
        <div className="text-xs text-gray-300 font-medium px-1 leading-tight">
          {data.name}
        </div>
      </div>
    </div>
  )
}
