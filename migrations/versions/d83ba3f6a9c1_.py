"""empty message

Revision ID: d83ba3f6a9c1
Revises: 
Create Date: 2019-06-23 20:25:22.268037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd83ba3f6a9c1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=400), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=80), nullable=True),
    sa.Column('nextqID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['nextqID'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nextqID')
    )
    op.create_table('games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character', sa.String(length=80), nullable=True),
    sa.Column('text', sa.String(length=200), nullable=True),
    sa.Column('firstqID', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['firstqID'], ['question.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('firstqID')
    )
    op.create_table('que_ans',
    sa.Column('QueId', sa.Integer(), nullable=True),
    sa.Column('AnsId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['AnsId'], ['answer.id'], ),
    sa.ForeignKeyConstraint(['QueId'], ['question.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('que_ans')
    op.drop_table('games')
    op.drop_table('answer')
    op.drop_table('question')
    # ### end Alembic commands ###