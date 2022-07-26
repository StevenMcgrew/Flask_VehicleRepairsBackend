"""timestamp function and triggers

Revision ID: 70737fe92343
Revises: 5ca7952e405a
Create Date: 2022-07-25 20:38:00.529368

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70737fe92343'
down_revision = '5ca7952e405a'
branch_labels = None
depends_on = None


def upgrade():
    op.execute(
        """
        CREATE OR REPLACE FUNCTION set_updated_on()
        RETURNS TRIGGER AS
        $$
            BEGIN
                NEW.updated_on = CURRENT_TIMESTAMP;
                RETURN NEW;
            END;
        $$
        LANGUAGE plpgsql;

        CREATE TRIGGER update_timestamp BEFORE UPDATE ON users FOR EACH ROW EXECUTE PROCEDURE set_updated_on();
        CREATE TRIGGER update_timestamp BEFORE UPDATE ON posts FOR EACH ROW EXECUTE PROCEDURE set_updated_on();
        CREATE TRIGGER update_timestamp BEFORE UPDATE ON comments FOR EACH ROW EXECUTE PROCEDURE set_updated_on();
        """
    )


def downgrade():
    op.execute(
        """
        DROP TRIGGER update_timestamp ON comments;
        DROP TRIGGER update_timestamp ON posts;
        DROP TRIGGER update_timestamp ON users;

        DROP FUNCTION set_updated_on();
        """
    )
