"""empty message

Revision ID: 9a9757ebe420
Revises: 9fe13968ba82
Create Date: 2018-04-22 08:32:08.703381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a9757ebe420'
down_revision = '9fe13968ba82'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cartinfo', sa.Column('total', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('cartinfo', 'total')
    # ### end Alembic commands ###
