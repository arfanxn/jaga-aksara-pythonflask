"""create_transliterations_table

Revision ID: 4157480430d9
Revises: a2787b7d726a
Create Date: 2024-11-07 18:36:22.104543

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4157480430d9'
down_revision: Union[str, None] = 'a2787b7d726a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'transliterations',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.CHAR(36), nullable=False),
        sa.Column('photo', sa.CHAR(32), nullable=False),
        sa.Column('result', sa.Text, nullable=False),
        sa.Column('impression', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime),
    )    
    op.create_foreign_key('user_id_3', 'transliterations', 'users', ['user_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')
    pass


def downgrade() -> None:
    op.drop_table('transliterations')
    pass
