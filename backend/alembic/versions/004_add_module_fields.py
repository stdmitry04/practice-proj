"""Add module fields to roadmap_nodes

Revision ID: 004
Revises: 003
Create Date: 2026-01-28 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '004'
down_revision: Union[str, None] = '003'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add node_type column for distinguishing concept nodes from module test nodes
    op.add_column('roadmap_nodes', sa.Column('node_type', sa.String(20), nullable=False, server_default='concept'))

    # Add module_order column for determining module sequence (1-9 for Python)
    op.add_column('roadmap_nodes', sa.Column('module_order', sa.Integer, nullable=True))

    # Add theory column for textbook-level theory content (markdown)
    op.add_column('roadmap_nodes', sa.Column('theory', sa.Text, nullable=True))

    # Create indexes for efficient queries
    op.create_index('ix_roadmap_nodes_node_type', 'roadmap_nodes', ['node_type'])
    op.create_index('ix_roadmap_nodes_language_module', 'roadmap_nodes', ['language_id', 'module_order'])
    op.create_index('ix_roadmap_nodes_topic_type', 'roadmap_nodes', ['topic', 'node_type'])


def downgrade() -> None:
    op.drop_index('ix_roadmap_nodes_topic_type', 'roadmap_nodes')
    op.drop_index('ix_roadmap_nodes_language_module', 'roadmap_nodes')
    op.drop_index('ix_roadmap_nodes_node_type', 'roadmap_nodes')
    op.drop_column('roadmap_nodes', 'theory')
    op.drop_column('roadmap_nodes', 'module_order')
    op.drop_column('roadmap_nodes', 'node_type')
