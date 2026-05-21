"""add_cpf_to_users

Revision ID: 3fd660bc6f01
Revises: 3ca20b5b7cb6
Create Date: 2026-05-21 18:15:19.678412

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3fd660bc6f01'
down_revision: Union[str, Sequence[str], None] = '3ca20b5b7cb6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Usa batch mode para compatibilidade com SQLite (copy-and-move strategy).
    with op.batch_alter_table('users') as batch_op:
        batch_op.add_column(sa.Column('cpf', sa.String(), nullable=True))
        batch_op.create_unique_constraint('uq_users_cpf', ['cpf'])


def downgrade() -> None:
    """Downgrade schema."""
    with op.batch_alter_table('users') as batch_op:
        batch_op.drop_constraint('uq_users_cpf', type_='unique')
        batch_op.drop_column('cpf')
