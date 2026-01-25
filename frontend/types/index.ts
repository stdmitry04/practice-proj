export interface Language {
  id: string
  name: string
  slug: string
  icon: string | null
  created_at: string
}

export interface Topic {
  id: string
  language_id: string
  name: string
  slug: string
  description: string | null
  difficulty: 'easy' | 'medium' | 'hard'
  created_at: string
}

export interface TestCase {
  name: string
  input: string
  expected_output: string
  hidden: boolean
}

export interface TestCasesConfig {
  test_cases: TestCase[]
  entry_point: string | null
  timeout_ms: number
}

export interface Exercise {
  id: string
  topic_id: string
  title: string
  description: string
  template_code: string
  solution_code: string
  test_cases: TestCasesConfig
  hints: string[] | null
  created_at: string
}

export interface TestCaseResult {
  name: string
  passed: boolean
  expected: string | null
  actual: string | null
  error: string | null
}

export interface SubmitResult {
  passed: boolean
  results: TestCaseResult[]
  compile_error: string | null
  runtime_error: string | null
}
