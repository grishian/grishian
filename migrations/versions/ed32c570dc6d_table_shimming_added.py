"""table Shimming added

Revision ID: ed32c570dc6d
Revises: e42fe5afc7ff
Create Date: 2023-11-30 15:50:34.466353

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed32c570dc6d'
down_revision = 'e42fe5afc7ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shimming',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pinion_value', sa.String(length=50), nullable=False),
    sa.Column('backlash_value', sa.String(length=255), nullable=True),
    sa.Column('shim_left', sa.Boolean(), nullable=True),
    sa.Column('shim_right', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shimming')
    # ### end Alembic commands ###
