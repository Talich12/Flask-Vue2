"""add_jwt_blacklist

Revision ID: 45e33df9e2ba
Revises: 2298ae8eaf35
Create Date: 2023-04-27 22:08:55.990558

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45e33df9e2ba'
down_revision = '2298ae8eaf35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('revoked_token_model',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_index('ix_user_token')
        batch_op.drop_column('token')
        batch_op.drop_column('token_expiration')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('token_expiration', sa.DATETIME(), nullable=True))
        batch_op.add_column(sa.Column('token', sa.VARCHAR(length=32), nullable=True))
        batch_op.create_index('ix_user_token', ['token'], unique=False)

    op.drop_table('revoked_token_model')
    # ### end Alembic commands ###
