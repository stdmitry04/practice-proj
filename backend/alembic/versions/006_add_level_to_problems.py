"""add level to problems

Revision ID: 006
Revises: 005
Create Date: 2026-01-28

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '006'
down_revision = '005'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Add level column to roadmap_problems
    op.add_column('roadmap_problems',
                  sa.Column('level', sa.String(20), nullable=False, server_default='beginner'))


def downgrade() -> None:
    op.drop_column('roadmap_problems', 'level')
