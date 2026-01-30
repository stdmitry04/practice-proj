import React from 'react'
import { ModuleCompletion, NodeTopic } from '@/types/roadmap'

interface ModuleListProps {
  modules: ModuleCompletion[]
}

// Topic colors mapping
const topicColors: Record<string, string> = {
  fundamentals: 'bg-blue-500',
  oop: 'bg-purple-500',
  'data-structures': 'bg-cyan-500',
  tooling: 'bg-orange-500',
  web: 'bg-emerald-500',
  database: 'bg-amber-500',
  'data-science': 'bg-pink-500',
  concurrency: 'bg-red-500',
  typing: 'bg-indigo-500',
}

const topicDisplayNames: Record<string, string> = {
  fundamentals: 'Fundamentals',
  oop: 'OOP',
  'data-structures': 'Data Structures',
  tooling: 'Tooling',
  web: 'Web',
  database: 'Database',
  'data-science': 'Data Science',
  concurrency: 'Concurrency',
  typing: 'Typing',
}

export function ModuleList({ modules }: ModuleListProps) {
  // Sort modules by module_order
  const sortedModules = [...modules].sort((a, b) => a.module_order - b.module_order)

  return (
    <div className="absolute top-4 left-4 z-10 bg-gray-900/95 border border-gray-700 rounded-lg p-4 shadow-xl max-w-xs">
      <h3 className="text-sm font-semibold text-gray-100 mb-3">Modules</h3>
      <div className="space-y-2">
        {sortedModules.map((module) => {
          const colorClass = topicColors[module.module_name] || 'bg-gray-500'
          const displayName = topicDisplayNames[module.module_name] || module.module_name

          return (
            <div key={module.module_name} className="flex items-center gap-2">
              {/* Colored line indicator */}
              <div className={`w-1 h-6 ${colorClass} rounded-full flex-shrink-0`}></div>

              {/* Module info */}
              <div className="flex-1 min-w-0">
                <div className="flex items-center justify-between gap-2">
                  <span className="text-sm text-gray-200 truncate">{displayName}</span>
                  {module.is_complete && (
                    <span className="text-green-400 text-xs flex-shrink-0">✓</span>
                  )}
                  {!module.is_complete && (
                    <span className="text-gray-500 text-xs flex-shrink-0">
                      {module.hard_problems_solved}/1
                    </span>
                  )}
                </div>
              </div>
            </div>
          )
        })}
      </div>

      {/* Legend */}
      <div className="mt-4 pt-3 border-t border-gray-700">
        <p className="text-xs text-gray-400">
          Complete module tests to unlock the next module
        </p>
      </div>
    </div>
  )
}
