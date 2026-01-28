'use client'

import { memo } from 'react'
import { Handle, Position, NodeProps } from 'reactflow'
import { RoadmapNodeWithProgress } from '@/types/roadmap'
import { clsx } from 'clsx'

function CustomNodeComponent({ data: node }: NodeProps<RoadmapNodeWithProgress>) {

  const hasProgress = node.easy_count > 0 || node.medium_count > 0 || node.hard_count > 0
  const isComplete =
    (node.easy_count === 0 || node.easy_solved === node.easy_count) &&
    (node.medium_count === 0 || node.medium_solved === node.medium_count) &&
    (node.hard_count === 0 || node.hard_solved === node.hard_count) &&
    hasProgress

  return (
    <div
      className={clsx(
        'px-4 py-3 rounded-lg border-2 cursor-pointer transition-all',
        'hover:shadow-lg hover:scale-105',
        'min-w-[180px] max-w-[220px]',
        isComplete
          ? 'bg-green-900/40 border-green-500'
          : hasProgress
          ? 'bg-blue-900/40 border-blue-500'
          : 'bg-gray-800 border-gray-600'
      )}
    >
      <Handle type="target" position={Position.Top} className="!bg-gray-500" />

      <div className="text-center">
        <h3 className="font-semibold text-gray-100 text-sm mb-2">{node.name}</h3>

        {hasProgress && (
          <div className="flex justify-center gap-2 text-xs">
            <span
              className={clsx(
                'px-2 py-0.5 rounded',
                node.easy_solved === node.easy_count && node.easy_count > 0
                  ? 'bg-green-700 text-green-200'
                  : 'bg-green-900/50 text-green-400'
              )}
            >
              E: {node.easy_solved}/{node.easy_count}
            </span>
            <span
              className={clsx(
                'px-2 py-0.5 rounded',
                node.medium_solved === node.medium_count && node.medium_count > 0
                  ? 'bg-yellow-700 text-yellow-200'
                  : 'bg-yellow-900/50 text-yellow-400'
              )}
            >
              M: {node.medium_solved}/{node.medium_count}
            </span>
            <span
              className={clsx(
                'px-2 py-0.5 rounded',
                node.hard_solved === node.hard_count && node.hard_count > 0
                  ? 'bg-red-700 text-red-200'
                  : 'bg-red-900/50 text-red-400'
              )}
            >
              H: {node.hard_solved}/{node.hard_count}
            </span>
          </div>
        )}

        {!hasProgress && (
          <div className="text-xs text-gray-500">No problems yet</div>
        )}
      </div>

      <Handle type="source" position={Position.Bottom} className="!bg-gray-500" />
    </div>
  )
}

export const CustomNode = memo(CustomNodeComponent)
