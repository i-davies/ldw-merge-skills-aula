"""Criar tabelas users, question_attempts e lesson_progress

Revision ID: 002
Revises: 001
Create Date: 2026-03-15
"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = '002'
down_revision: Union[str, None] = '001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, unique=True, nullable=False),
    )

    op.create_table(
        'question_attempts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer,
                  sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('question_id', sa.Integer,
                  sa.ForeignKey('questions.id', ondelete='CASCADE'), nullable=False),
        sa.Column('selected_option', sa.Integer, nullable=False),
        sa.Column('is_correct', sa.Boolean, default=False),
        sa.Column('timestamp', sa.DateTime, server_default=sa.func.now()),
    )

    op.create_table(
        'lesson_progress',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer,
                  sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('lesson_id', sa.Integer,
                  sa.ForeignKey('lessons.id', ondelete='CASCADE'), nullable=False),
        sa.Column('is_completed', sa.Boolean, default=False),
        sa.Column('completed_at', sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table('lesson_progress')
    op.drop_table('question_attempts')
    op.drop_table('users')