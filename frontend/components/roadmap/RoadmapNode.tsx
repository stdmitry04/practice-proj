'use client'

import { memo } from 'react'
import { Handle, Position, NodeProps } from 'reactflow'
import { RoadmapNodeWithProgress } from '@/types/roadmap'
import { clsx } from 'clsx'

interface RoadmapNodeData {
  node: RoadmapNodeWithProgress
  onClick: (node: RoadmapNodeWithProgress) => void
}

function RoadmapNodeComponent({ data }: NodeProps<RoadmapNodeData>) {
  const { node, onClick } = data

  const hasProgress = node.easy_count > 0 || node.medium_count > 0 || node.hard_count > 0
  const isComplete =
    (node.easy_count === 0 || node.easy_solved === node.easy_count) &&
    (node.medium_count === 0 || node.medium_solved === node.medium_count) &&
    (node.hard_count === 0 || node.hard_solved === node.hard_count) &&
    hasProgress

  return (
    <div
      onClick={() => onClick(node)}
      className={clsx(
        'px-4 py-3 rounded-lg border-2 cursor-pointer transition-all',
        'hover:shadow-lg hover:scale-105',
        'min-w-[180px] max-w-[220px]',
        isComplete
          ? 'bg-green-50 border-green-400'
          : hasProgress
          ? 'bg-blue-50 border-blue-400'
          : 'bg-white border-gray-300'
      )}
    >
      <Handle type="target" position={Position.Top} className="!bg-gray-400" />

      <div className="text-center">
        <h3 className="font-semibold text-gray-800 text-sm mb-2">{node.name}</h3>

        {hasProgress && (
          <div className="flex justify-center gap-2 text-xs">
            <span
              className={clsx(
                'px-2 py-0.5 rounded',
                node.easy_solved === node.easy_count && node.easy_count > 0
                  ? 'bg-green-200 text-green-800'
                  : 'bg-green-100 text-green-700'
              )}
            >
              E: {node.easy_solved}/{node.easy_count}
            </span>
            <span
              className={clsx(
                'px-2 py-0.5 rounded',
                node.medium_solved === node.medium_count && node.medium_count > 0
                  ? 'bg-yellow-200 text-yellow-800'
                  : 'bg-yellow-100 text-yellow-700'
              )}
            >
              M: {node.medium_solved}/{node.medium_count}
            </span>
            <span
              className={clsx(
                'px-2 py-0.5 rounded',
                node.hard_solved === node.hard_count && node.hard_count > 0
                  ? 'bg-red-200 text-red-800'
                  : 'bg-red-100 text-red-700'
              )}
            >
              H: {node.hard_solved}/{node.hard_count}
            </span>
          </div>
        )}

        {!hasProgress && (
          <div className="text-xs text-gray-400">No problems yet</div>
        )}
      </div>

      <Handle type="source" position={Position.Bottom} className="!bg-gray-400" />
    </div>
  )
}

export default memo(RoadmapNodeComponent)
