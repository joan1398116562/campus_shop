"""empty message

Revision ID: d88cbaaede96
Revises: 09cfa5c6730a
Create Date: 2018-04-22 21:38:02.785186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd88cbaaede96'
down_revision = '09cfa5c6730a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('orderinfo', sa.Column('total', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('orderinfo', 'total')
    # ### end Alembic commands ###
