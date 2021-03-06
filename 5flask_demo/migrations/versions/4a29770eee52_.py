"""empty message

Revision ID: 4a29770eee52
Revises: ade665b7022a
Create Date: 2019-04-24 17:01:19.518388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a29770eee52'
down_revision = 'ade665b7022a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chapter', sa.Column('book_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'chapter', 'book', ['book_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'chapter', type_='foreignkey')
    op.drop_column('chapter', 'book_id')
    # ### end Alembic commands ###
