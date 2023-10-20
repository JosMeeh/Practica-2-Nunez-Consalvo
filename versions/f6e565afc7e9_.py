"""empty message

Revision ID: f6e565afc7e9
Revises: 69eb8e5b8dde
Create Date: 2023-10-20 18:58:46.230337

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f6e565afc7e9'
down_revision: Union[str, None] = '69eb8e5b8dde'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
