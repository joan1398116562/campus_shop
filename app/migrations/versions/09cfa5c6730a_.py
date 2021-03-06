"""empty message

Revision ID: 09cfa5c6730a
Revises: 4e8addbff67d
Create Date: 2018-04-22 16:27:15.004528

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09cfa5c6730a'
down_revision = '4e8addbff67d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('add_time', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cart_add_time'), 'cart', ['add_time'], unique=False)
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('add_time', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('subTotal', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_order_add_time'), 'order', ['add_time'], unique=False)
    op.create_table('cartinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('product_name', sa.String(length=100), nullable=True),
    sa.Column('product_price', sa.Float(), nullable=True),
    sa.Column('total', sa.Float(), nullable=True),
    sa.Column('add_time', sa.DateTime(), nullable=True),
    sa.Column('cart_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cartinfo_add_time'), 'cartinfo', ['add_time'], unique=False)
    op.create_table('orderinfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('product_name', sa.String(length=100), nullable=True),
    sa.Column('product_price', sa.Float(), nullable=True),
    sa.Column('add_time', sa.DateTime(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_orderinfo_add_time'), 'orderinfo', ['add_time'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_orderinfo_add_time'), table_name='orderinfo')
    op.drop_table('orderinfo')
    op.drop_index(op.f('ix_cartinfo_add_time'), table_name='cartinfo')
    op.drop_table('cartinfo')
    op.drop_index(op.f('ix_order_add_time'), table_name='order')
    op.drop_table('order')
    op.drop_index(op.f('ix_cart_add_time'), table_name='cart')
    op.drop_table('cart')
    # ### end Alembic commands ###
