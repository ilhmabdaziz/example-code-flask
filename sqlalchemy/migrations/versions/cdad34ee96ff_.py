"""empty message

Revision ID: cdad34ee96ff
Revises: 22ce8aaa1319
Create Date: 2024-05-06 21:18:14.418520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cdad34ee96ff'
down_revision = '22ce8aaa1319'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('departments',
    sa.Column('dept_no', sa.String(length=20), nullable=False),
    sa.Column('dept_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('dept_no')
    )
    op.create_table('dept_emp',
    sa.Column('emp_no', sa.Integer(), nullable=False),
    sa.Column('dept_no', sa.String(length=20), nullable=False),
    sa.Column('from_date', sa.Date(), nullable=False),
    sa.Column('to_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['dept_no'], ['departments.dept_no'], ),
    sa.ForeignKeyConstraint(['emp_no'], ['employees.emp_no'], ),
    sa.PrimaryKeyConstraint('emp_no', 'dept_no')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dept_emp')
    op.drop_table('departments')
    # ### end Alembic commands ###
