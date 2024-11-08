"""create_updates_table

Revision ID: 0a9a3bc765ce
Revises: 75fd08ca5c29
Create Date: 2024-11-07 19:15:27.595986

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a9a3bc765ce'
down_revision: Union[str, None] = '75fd08ca5c29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'updates',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.CHAR(36), nullable=False),
        sa.Column('version', sa.Integer, nullable=False), 
        sa.Column('note', sa.TEXT, nullable=False), 
        sa.Column('created_at', sa.DateTime, nullable=False, default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime),
    )    
    pass


def downgrade() -> None:
    op.drop_table('updates')
    pass
