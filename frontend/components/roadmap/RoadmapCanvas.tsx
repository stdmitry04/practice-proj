'use client'

import {useEffect, useMemo} from 'react'
import ReactFlow, {
    Background,
    Controls,
    useNodesState,
    useEdgesState,
    MarkerType,
} from 'reactflow'
import 'reactflow/dist/style.css'

import { CustomNode } from './CustomNode'
import { RoadmapNodeWithProgress } from '@/types/roadmap'

// Define nodeTypes outside the component to avoid recreation on each render
const nodeTypes = {
    custom: CustomNode,
}

interface RoadmapCanvasProps {
    nodes: RoadmapNodeWithProgress[]
    onNodeClick: (node: RoadmapNodeWithProgress) => void
}

export function RoadmapCanvas({ nodes: roadmapNodes, onNodeClick }: RoadmapCanvasProps) {
    // Convert roadmap nodes to ReactFlow nodes
    const initialNodes = useMemo(() => {
        return roadmapNodes.map((node) => ({
            id: node.id,
            type: 'custom',
            position: { x: node.position_x, y: node.position_y },
            data: node,
        }))
    }, [roadmapNodes])

    // Create edges from parent-child relationships
    const initialEdges = useMemo(() => {
        return roadmapNodes
            .filter((node) => node.parent_id)
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


    const handleNodeClick = (_: React.MouseEvent, node: { data: RoadmapNodeWithProgress }) => {
        onNodeClick(node.data)
    }

    return (
        <div style={{ width: '100%', height: 'calc(100vh - 64px)' }}>
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