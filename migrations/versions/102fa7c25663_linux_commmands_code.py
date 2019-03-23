"""linux commmands code

Revision ID: 102fa7c25663
Revises: ad874d620dc5
Create Date: 2019-03-22 18:00:55.896009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '102fa7c25663'
down_revision = 'ad874d620dc5'
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