"""Create an error model

Revision ID: 6a68e3a5c60a
Revises: 5a434965d6a4
Create Date: 2024-02-21 11:46:51.403623

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "6a68e3a5c60a"
down_revision: Union[str, None] = "5a434965d6a4"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "errors",
        sa.Column("error_id", sa.BIGINT(), autoincrement=True, nullable=False),
        sa.Column("user_id", sa.BIGINT(), nullable=False),
        sa.Column("username", sa.String(length=128), nullable=True),
        sa.Column("error_message", sa.String(length=1000)),
        sa.Column("status", sa.String(), server_default="New"),
        sa.Column("software", sa.String()),
        sa.ForeignKeyConstraint(["user_id"], ["users.user_id"]),
        sa.PrimaryKeyConstraint("error_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("errors")
    # ### end Alembic commands ###
