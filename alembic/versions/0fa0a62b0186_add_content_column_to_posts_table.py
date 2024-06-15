"""Add content column to posts table.

Revision ID: 0fa0a62b0186
Revises: b42546ef83ef
Create Date: 2024-06-15 17:27:07.146240

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0fa0a62b0186'
down_revision: Union[str, None] = 'b42546ef83ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
