"""create_personal_access_tokens_table

Revision ID: ab95f9c33f94
Revises: 944791bd1094
Create Date: 2024-10-01 13:02:36.366251

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = 'ab95f9c33f94'
down_revision: Union[str, None] = '944791bd1094'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'personal_access_tokens',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('name', sa.Enum('jwt', 'others'), nullable=False),
        sa.Column('secret', sa.String(255), nullable=False),
        sa.Column('redirect', sa.String(255), nullable=True),
        sa.Column('revoked_at', sa.DateTime, nullable=True),
        sa.Column('created_at', sa.DateTime, nullable=False, default=func.now()),
        sa.Column('updated_at', sa.DateTime),
    )    
    op.create_foreign_key('user_id', 'personal_access_tokens', 'users', ['user_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')
    pass


def downgrade() -> None:
    op.drop_table('personal_access_tokens')
    pass
