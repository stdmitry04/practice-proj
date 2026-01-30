'use client'

import {useEffect, useMemo, useState} from 'react'
import ReactFlow, {
    Background,
    Controls,
    useNodesState,
    useEdgesState,
    MarkerType,
} from 'reactflow'
import 'reactflow/dist/style.css'

import { CustomNode } from './CustomNode'
import { HexagonalNode } from './HexagonalNode'
import { ModuleList } from './ModuleList'
import { RoadmapNodeWithProgress, ModuleCompletion } from '@/types/roadmap'
import { api } from '@/lib/api'

// Define nodeTypes outside the component to avoid recreation on each render
const nodeTypes = {
    custom: CustomNode,
    hexagonal: HexagonalNode,
}

interface RoadmapCanvasProps {
    nodes: RoadmapNodeWithProgress[]
    languageId: string
    onNodeClick: (node: RoadmapNodeWithProgress) => void
}

export function RoadmapCanvas({ nodes: roadmapNodes, languageId, onNodeClick }: RoadmapCanvasProps) {
    const [moduleCompletions, setModuleCompletions] = useState<ModuleCompletion[]>([])

    // Fetch module completion data
    useEffect(() => {
        async function fetchModuleCompletions() {
            try {
                const data = await api.getModuleCompletions(languageId)
                setModuleCompletions(data)
            } catch (error) {
                console.error('Failed to fetch module completions:', error)
            }
        }
        if (languageId) {
            fetchModuleCompletions()
        }
    }, [languageId, roadmapNodes])

    // Calculate if a node is locked based on module completion
    const calculateIsLocked = (_node: RoadmapNodeWithProgress): boolean => {
        // All concepts are unlocked
        return false
    }

    // Convert roadmap nodes to ReactFlow nodes with locking logic
    const initialNodes = useMemo(() => {
        return roadmapNodes.map((node) => {
            const isLocked = calculateIsLocked(node)
            const nodeType = node.node_type === 'module_test' ? 'hexagonal' : 'custom'

            return {
                id: node.id,
                type: nodeType,
                position: { x: node.position_x, y: node.position_y },
                data: {
                    ...node,
                    is_locked: isLocked,
                    onClick: (nodeId: string) => {
                        const clickedNode = roadmapNodes.find(n => n.id === nodeId)
                        if (clickedNode) {
                            if (isLocked) {
                                // Find the blocking module
                                const nodeModule = moduleCompletions.find(m => m.module_name === clickedNode.topic)
                                if (nodeModule) {
                                    const previousIncomplete = moduleCompletions
                                        .filter(m => m.module_order < nodeModule.module_order && !m.is_complete)
                                        .sort((a, b) => a.module_order - b.module_order)

                                    if (previousIncomplete.length > 0) {
                                        const blockingModule = previousIncomplete[0].module_name
                                        alert(`🔒 Complete the ${blockingModule} module test to unlock this node`)
                                    }
                                }
                            } else {
                                onNodeClick(clickedNode)
                            }
                        }
                    }
                },
            }
        })
    }, [roadmapNodes, moduleCompletions, onNodeClick])

    // Create edges from parent-child relationships (exclude module_test nodes which have no parent)
    const initialEdges = useMemo(() => {
        return roadmapNodes
            .filter((node) => node.parent_id && node.node_type !== 'module_test')
            .map((node) => ({
                id: `${node.parent_id}-${node.id}`,
                source: node.parent_id!,
                target: node.id,
                type: 'smoothstep',
                animated: false,
                style: { stroke: '#4b5563', strokeWidth: 2 },
                markerEnd: {
                    type: MarkerType.ArrowClosed,
                    color: '#4b5563',
                },
            }))
    }, [roadmapNodes])

    const [nodes, setNodes, onNodesChange] = useNodesState(initialNodes)
    const [edges, setEdges, onEdgesChange] = useEdgesState(initialEdges)

    // This updates the graph when the parent data (roadmapNodes) changes
    useEffect(() => {
        setNodes(initialNodes)
        setEdges(initialEdges)
    }, [initialNodes, initialEdges, setNodes, setEdges])
    // -----------------------


    const handleNodeClick = (_: React.MouseEvent, node: { data: any }) => {
        if (node.data.onClick) {
            node.data.onClick(node.data.id)
        }
    }

    return (
        <div style={{ width: '100%', height: 'calc(100vh - 64px)', position: 'relative' }}>
            {/* Module List */}
            {moduleCompletions.length > 0 && <ModuleList modules={moduleCompletions} />}

            <ReactFlow
                nodes={nodes}
                edges={edges}
                onNodesChange={onNodesChange}
                onEdgesChange={onEdgesChange}
                onNodeClick={handleNodeClick}
                nodeTypes={nodeTypes}
                fitView
                fitViewOptions={{ padding: 0.2 }}
                minZoom={0.5}
                maxZoom={1.5}
                nodesDraggable={false}
                nodesConnectable={false}
            >
                <Background color="#374151" gap={20} />
                <Controls showInteractive={false} />
            </ReactFlow>
        </div>
    )
}