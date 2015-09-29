"""added orientation column to pi model

Revision ID: 2711340c6d9d
Revises: 490d49497045
Create Date: 2015-09-25 09:43:33.202018

"""

# revision identifiers, used by Alembic.
revision = '2711340c6d9d'
down_revision = '490d49497045'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('PiUrl', sa.Column('orientation', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('PiUrl', 'orientation')
    ### end Alembic commands ###
