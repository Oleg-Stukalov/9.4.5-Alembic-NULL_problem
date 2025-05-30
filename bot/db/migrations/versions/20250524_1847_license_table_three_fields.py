"""License table-THREE fields

Revision ID: 31ba8d2379b7
Revises:
Create Date: 2025-05-24 18:47:46.938285

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31ba8d2379b7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('licenses',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('licenses')
    # ### end Alembic commands ###
