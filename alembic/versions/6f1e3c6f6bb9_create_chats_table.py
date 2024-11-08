"""create_chats_table

Revision ID: 6f1e3c6f6bb9
Revises: 4157480430d9
Create Date: 2024-11-07 19:03:55.494273

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f1e3c6f6bb9'
down_revision: Union[str, None] = '4157480430d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'chats',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.CHAR(36), nullable=False),
        sa.Column('question', sa.Text, nullable=False),
        sa.Column('answer', sa.Text, nullable=False),
        sa.Column('status', sa.Enum('active', 'deleted'), nullable=False, default='active'),
        sa.Column('created_at', sa.DateTime, nullable=False, default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime),
        # sa.Column('deleted_at', sa.DateTime),
    )    
    op.create_foreign_key('user_id_4', 'chats', 'users', ['user_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')
    pass


def downgrade() -> None:
    op.drop_table('chats')
    pass
