"""tags table

Revision ID: 16ec71f26515
Revises: e36200a2f563
Create Date: 2022-07-25 17:09:33.824069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '16ec71f26515'
down_revision = 'e36200a2f563'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('tag', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('tag')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    # ### end Alembic commands ###