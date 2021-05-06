"""create_main_tables

Revision ID: 7cafe6bf8373
Revises:
Create Date: 2021-04-19 00:37:05.394433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '7cafe6bf8373'
down_revision = None
branch_labels = None
depends_on = None


def create_games_table() -> None:
    op.create_table(
        "games",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True, index=False)
    )


def upgrade() -> None:
    create_games_table()


def downgrade() -> None:
    op.drop_table("games")
