"""create users table

Revision ID: d6901b637367
Revises: 
Create Date: 2022-07-25 12:45:23.662183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6901b637367'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=319), nullable=False),
    sa.Column('username', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('type', sa.String(length=20), nullable=False),
    sa.Column('status', sa.String(length=20), nullable=False),
    sa.Column('profile_pic', sa.String(length=255), nullable=True),
    sa.Column('vehicles_history', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('views_history', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('following', sa.ARRAY(sa.Integer()), nullable=True),
    sa.Column('prefers_notifications', sa.Boolean(), nullable=False),
    sa.Column('theme', sa.String(length=20), nullable=False),
    sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
