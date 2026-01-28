'use client'

import { useRef, useEffect, useCallback } from 'react'
import Editor, { OnMount } from '@monaco-editor/react'
import { usePracticeStore } from '@/stores/practiceStore'

const LANGUAGE_MAP: Record<string, string> = {
  react: 'javascript',
  javascript: 'javascript',
  python: 'python',
  cpp: 'cpp',
}

export function CodeEditor() {
  const editorRef = useRef<any>(null)
  const containerRef = useRef<HTMLDivElement>(null)
  const { selectedLanguage, currentExercise, code, setCode } = usePracticeStore()

  const handleEditorMount: OnMount = (editor) => {
    editorRef.current = editor
  }

  const handleEditorChange = (value: string | undefined) => {
    setCode(value || '')
  }

  // Handle mouse enter/leave to toggle body scroll behavior
  const handleMouseEnter = useCallback(() => {
    document.body.style.overflow = 'auto'
  }, [])

  const handleMouseLeave = useCallback(() => {
    document.body.style.overflow = ''
  }, [])

  useEffect(() => {
    if (editorRef.current && currentExercise) {
      editorRef.current.setValue(currentExercise.template_code)
    }
  }, [currentExercise])

  // Cleanup on unmount
  useEffect(() => {
    return () => {
      document.body.style.overflow = ''
    }
  }, [])

  const language = selectedLanguage
    ? LANGUAGE_MAP[selectedLanguage.slug] || 'plaintext'
    : 'plaintext'

  if (!currentExercise) {
    return (
      <div className="h-full flex items-center justify-center bg-slate-900 text-slate-400">
        <div className="text-center">
          <div className="text-4xl mb-4">💻</div>
          <p>Generate an exercise to start coding</p>
        </div>
      </div>
    )
  }

  return (
    <div
      ref={containerRef}
      className="h-full flex flex-col"
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
    >
      <div className="bg-slate-800 px-4 py-2 text-sm text-slate-300 flex items-center justify-between">
        <span>Editor - {selectedLanguage?.name || 'Unknown'}</span>
        <span className="text-xs text-slate-500">
          Press Ctrl+S to format (if supported)
        </span>
      </div>
      <div className="flex-1">
        <Editor
          height="100%"
          language={language}
          value={code}
          onChange={handleEditorChange}
          onMount={handleEditorMount}
          theme="vs-dark"
          options={{
            fontSize: 14,
            fontFamily: 'JetBrains Mono, Menlo, Monaco, monospace',
            minimap: { enabled: false },
            scrollBeyondLastLine: false,
            lineNumbers: 'on',
            renderLineHighlight: 'all',
            automaticLayout: true,
            tabSize: 2,
            wordWrap: 'on',
            padding: { top: 16, bottom: 16 },
          }}
        />
      </div>
    </div>
  )
}
