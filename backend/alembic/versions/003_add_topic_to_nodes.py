"""Add topic column to roadmap_nodes

Revision ID: 003
Revises: 002
Create Date: 2024-01-20 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '003'
down_revision: Union[str, None] = '002'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add topic column for visual grouping of nodes
    op.add_column('roadmap_nodes', sa.Column('topic', sa.String(50), nullable=True))


def downgrade() -> None:
    op.drop_column('roadmap_nodes', 'topic')
