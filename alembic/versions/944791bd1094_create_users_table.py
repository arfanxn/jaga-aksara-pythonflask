"""Create users table

Revision ID: 944791bd1094
Revises: 
Create Date: 2024-09-25 22:04:14.521368

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = '944791bd1094'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.CHAR(36), primary_key=True),
        sa.Column('country_code', sa.Integer, nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('phone', sa.String(16), unique=True, nullable=False),
        sa.Column('sex', sa.Enum('male', 'female'), nullable=False),
        sa.Column('level', sa.Enum('standard', 'admin'), nullable=False),
        sa.Column('birth_date', sa.DateTime, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False, default=func.now()),
        sa.Column('updated_at', sa.DateTime),
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
