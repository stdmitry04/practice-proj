"""add level-based content structure

Revision ID: 005
Revises: 004
Create Date: 2026-01-28

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '005'
down_revision = '004'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Change theory column to JSON to support multiple levels
    # Store as: {"beginner": "...", "intermediate": "...", "advanced": "...", "cheatsheet": "..."}
    op.alter_column('roadmap_nodes', 'theory',
                    type_=postgresql.JSON(astext_type=sa.Text()),
                    postgresql_using='jsonb_build_object(\'beginner\', theory)',
                    nullable=True)


def downgrade() -> None:
    # Revert back to text, taking only the beginner content
    op.alter_column('roadmap_nodes', 'theory',
                    type_=sa.Text(),
                    postgresql_using='theory->>\'beginner\'',
                    nullable=True)
