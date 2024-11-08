"""create_otps_table

Revision ID: 75fd08ca5c29
Revises: 6f1e3c6f6bb9
Create Date: 2024-11-07 19:08:40.640527

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75fd08ca5c29'
down_revision: Union[str, None] = '6f1e3c6f6bb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'otps',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_id', sa.CHAR(36), nullable=False),
        sa.Column('code', sa.Integer, nullable=False), 
        sa.Column('status', sa.Enum('available', 'used'), nullable=False, default='active'),
        sa.Column('created_at', sa.DateTime, nullable=False, default=sa.func.now()),
        sa.Column('updated_at', sa.DateTime),
    )    
    op.create_foreign_key('user_id_5', 'otps', 'users', ['user_id'], ['id'], ondelete='CASCADE', onupdate='CASCADE')
    pass


def downgrade() -> None:
    op.drop_table('otps')
    pass
