"""Add roadmap tables

Revision ID: 002
Revises: 001
Create Date: 2024-01-15 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '002'
down_revision: Union[str, None] = '001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create roadmap_nodes table
    op.create_table(
        'roadmap_nodes',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('language_id', sa.UUID(), nullable=False),
        sa.Column('name', sa.String(100), nullable=False),
        sa.Column('slug', sa.String(100), nullable=False),
        sa.Column('description', sa.Text(), nullable=True),
        sa.Column('position_x', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('position_y', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('parent_id', sa.UUID(), nullable=True),
        sa.Column('order_index', sa.Integer(), nullable=False, server_default='0'),
        sa.Column('concept_keywords', sa.JSON(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['language_id'], ['languages.id'], ondelete='CASCADE'),
        sa.ForeignKeyConstraint(['parent_id'], ['roadmap_nodes.id'], ondelete='SET NULL'),
        sa.PrimaryKeyConstraint('id')
    )

    # Create roadmap_problems table
    op.create_table(
        'roadmap_problems',
        sa.Column('id', sa.UUID(), nullable=False),
        sa.Column('node_id', sa.UUID(), nullable=False),
        sa.Column('difficulty', sa.Enum('easy', 'medium', 'hard', name='difficultyenum'), nullable=False),
        sa.Column('status', sa.Enum('unsolved', 'attempted', 'solved', name='statusenum'), nullable=False),
        sa.Column('title', sa.String(200), nullable=False),
        sa.Column('description', sa.Text(), nullable=False),
        sa.Column('template_code', sa.Text(), nullable=False),
        sa.Column('solution_code', sa.Text(), nullable=False),
        sa.Column('test_cases', sa.JSON(), nullable=False),
        sa.Column('hints', sa.JSON(), nullable=True),
        sa.Column('description_hash', sa.String(64), nullable=False, unique=True),
        sa.Column('condensed_description', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.ForeignKeyConstraint(['node_id'], ['roadmap_nodes.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )

    # Create index for faster lookups
    op.create_index('ix_roadmap_nodes_language_id', 'roadmap_nodes', ['language_id'])
    op.create_index('ix_roadmap_problems_node_id', 'roadmap_problems', ['node_id'])
    op.create_index('ix_roadmap_problems_difficulty', 'roadmap_problems', ['difficulty'])


def downgrade() -> None:
    op.drop_index('ix_roadmap_problems_difficulty')
    op.drop_index('ix_roadmap_problems_node_id')
    op.drop_index('ix_roadmap_nodes_language_id')
    op.drop_table('roadmap_problems')
    op.drop_table('roadmap_nodes')
    op.execute('DROP TYPE IF EXISTS difficultyenum')
    op.execute('DROP TYPE IF EXISTS statusenum')
