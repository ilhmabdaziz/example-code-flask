"""empty message

Revision ID: 22ce8aaa1319
Revises: 22865f86671f
Create Date: 2024-05-06 21:15:14.590996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22ce8aaa1319'
down_revision = '22865f86671f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('salaries', schema=None) as batch_op:
        batch_op.create_foreign_key(None, 'employees', ['emp_no'], ['emp_no'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('salaries', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')

    # ### end Alembic commands ###
