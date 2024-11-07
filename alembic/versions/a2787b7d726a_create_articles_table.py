"""create_articles_table

Revision ID: a2787b7d726a
Revises: 1f63a03e5706
Create Date: 2024-11-07 18:29:58.509187

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a2787b7d726a'
down_revision: Union[str, None] = '1f63a03e5706'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'articles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.CHAR(36), nullable=False),
        sa.Column('title', sa.String(60), nullable=False),
        sa.Column('thumbnail', sa.CHAR(32), nullable=False),
        sa.Column('content', sa.CHAR(32), nullable=False),
        sa.Column('impression', sa.Integer, nullable=False),
        sa.Column('view_time', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime),
    )    
    op.create_foreign_key('user_id_2', 'articles', 'users', ['user_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')
    pass


def downgrade() -> None:
    op.drop_table('articles')
    pass
