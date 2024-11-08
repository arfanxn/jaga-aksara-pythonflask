"""create_countries_table

Revision ID: 1f63a03e5706
Revises: ab95f9c33f94
Create Date: 2024-11-07 18:14:31.161277

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1f63a03e5706'
down_revision: Union[str, None] = 'ab95f9c33f94'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table (
        'countries',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('code', sa.Integer, nullable=False),
        sa.Column('name', sa.String(50), nullable=False),
    )
    pass


def downgrade() -> None:
    op.drop_table('countries')
    pass
