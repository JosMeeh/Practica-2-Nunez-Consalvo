"""initial migration

Revision ID: 69eb8e5b8dde
Revises: 
Create Date: 2023-10-20 18:36:08.844601

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '69eb8e5b8dde'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('directories',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('emails', sa.ARRAY(sa.String()), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_directories_id'), 'directories', ['id'], unique=False)
    op.create_index(op.f('ix_directories_name'), 'directories', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_directories_name'), table_name='directories')
    op.drop_index(op.f('ix_directories_id'), table_name='directories')
    op.drop_table('directories')
    # ### end Alembic commands ###
