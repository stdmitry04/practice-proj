export type Difficulty = 'easy' | 'medium' | 'hard'
export type ProblemStatus = 'unsolved' | 'attempted' | 'solved'
export type NodeType = 'concept' | 'module_test'
export type Level = 'beginner' | 'intermediate' | 'advanced' | 'cheatsheet'

export type NodeTopic =
  | 'fundamentals'
  | 'oop'
  | 'data-structures'
  | 'tooling'
  | 'web'
  | 'database'
  | 'data-science'
  | 'concurrency'
  | 'typing'

export interface RoadmapNode {
  id: string
  language_id: string
  name: string
  slug: string
  description: string | null
  position_x: number
  position_y: number
  parent_id: string | null
  order_index: number
  concept_keywords: string[] | null
  topic: NodeTopic | null
  node_type: NodeType
  module_order: number | null
  theory: {
    beginner?: string
    intermediate?: string
    advanced?: string
    cheatsheet?: string
  } | null
  created_at: string
}

export interface RoadmapNodeWithProgress extends RoadmapNode {
  easy_count: number
  medium_count: number
  hard_count: number
  easy_solved: number
  medium_solved: number
  hard_solved: number
  is_locked: boolean
}

export interface ModuleCompletion {
  module_name: string
  module_order: number
  is_complete: boolean
  nodes_complete: number
  nodes_total: number
  hard_problems_solved: number
}

export interface RoadmapProblem {
  id: string
  node_id: string
  difficulty: Difficulty
  level: Level
  status: ProblemStatus
  title: string
  description: string
  template_code: string
  solution_code: string
  test_cases: {
    test_cases: Array<{
      name: string
      input: string
      expected_output: string
      hidden: boolean
    }>
    entry_point: string | null
    timeout_ms: number
  }
  hints: string[] | null
  description_hash: string
  condensed_description: string
  created_at: string
}

export interface RoadmapProblemSummary {
  id: string
  title: string
  difficulty: Difficulty
  level: Level
  status: ProblemStatus
  created_at: string
}

export interface NodeProgress {
  easy_total: number
  easy_solved: number
  medium_total: number
  medium_solved: number
  hard_total: number
  hard_solved: number
}

export interface SubmitResult {
  passed: boolean
  results: Array<{
    name: string
    passed: boolean
    expected: string | null
    actual: string | null
    error: string | null
  }>
  compile_error: string | null
  runtime_error: string | null
}
