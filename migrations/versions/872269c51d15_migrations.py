"""migrations

Revision ID: 872269c51d15
Revises: 
Create Date: 2019-12-05 11:32:09.617663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '872269c51d15'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.Column('pass_secure', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=False)
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('author', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('posted', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('photo', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
