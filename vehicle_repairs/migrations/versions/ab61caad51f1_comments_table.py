"""comments table

Revision ID: ab61caad51f1
Revises: 91d557461b5d
Create Date: 2022-07-25 17:07:13.748541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab61caad51f1'
down_revision = '91d557461b5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('comment', sa.String(length=2000), nullable=False),
    sa.Column('like_count', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
