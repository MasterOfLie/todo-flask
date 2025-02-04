"""mudando banco de dados

Revision ID: e3d1ced7e0ac
Revises: 
Create Date: 2024-06-15 17:45:23.798225

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3d1ced7e0ac'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tarefas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=80), nullable=False),
    sa.Column('descricao', sa.String(length=120), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.Column('data_criacao', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tarefas')
    # ### end Alembic commands ###
