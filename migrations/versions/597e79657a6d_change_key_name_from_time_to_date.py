"""Change key name from time to date

Revision ID: 597e79657a6d
Revises: 85c6222c1a96
Create Date: 2020-07-27 19:28:02.763747

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '597e79657a6d'
down_revision = '85c6222c1a96'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('date', sa.String(length=64), nullable=True))
    op.drop_column('articles', 'time')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('articles', sa.Column('', mysql.VARCHAR(length=64), nullable=True))
    op.drop_column('articles', 'date')
    # ### end Alembic commands ###
