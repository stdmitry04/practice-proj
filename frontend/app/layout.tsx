import type { Metadata } from 'next'
import './globals.css'
import 'reactflow/dist/style.css'

export const metadata: Metadata = {
  title: 'Code Practice Platform',
  description: 'Practice coding exercises across React, JavaScript, Python, and C++',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="antialiased">{children}</body>
    </html>
  )
}
