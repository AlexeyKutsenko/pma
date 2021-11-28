"""Initial commit

Revision ID: 180e51240007
Revises: 
Create Date: 2021-11-28 03:06:41.441994

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '180e51240007'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('stock',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('code', sa.String(length=36), nullable=False),
    sa.Column('ticker', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('sector', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stock')
    # ### end Alembic commands ###