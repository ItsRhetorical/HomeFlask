"""linux commmands code2

Revision ID: a3dc7d06d9e2
Revises: 483bae604bc4
Create Date: 2019-03-23 21:44:55.214329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3dc7d06d9e2'
down_revision = '483bae604bc4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('linux_command', sa.Column('code', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('linux_command', 'code')
    # ### end Alembic commands ###
