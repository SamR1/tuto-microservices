"""empty message

Revision ID: 37da7639a818
Revises: daac9eff3b03
Create Date: 2017-11-03 16:04:04.847902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37da7639a818'
down_revision = 'daac9eff3b03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('admin', sa.Boolean(), nullable=False))
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password')
    op.drop_column('users', 'admin')
    # ### end Alembic commands ###