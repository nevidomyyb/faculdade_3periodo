"""empty message

Revision ID: cc688816ce63
Revises: 
Create Date: 2023-11-22 05:07:22.329281

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cc688816ce63'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ponto_vacinacao',
    sa.Column('idpontovacinacao', sa.String(length=36), nullable=False),
    sa.Column('nome', sa.String(length=248), nullable=False),
    sa.Column('bairro', sa.Enum('POÇO', 'JARAGUÁ', 'PONTA_DA_TERRA', 'PAJUÇARA', 'PONTA_VERDE', 'JATIÚCA', 'MANGABEIRAS', 'CENTRO', 'PONTAL_DA_BARRA', 'TRAPICHE', 'PRADO', 'PONTA_GROSSA', 'LEVADA', 'VERGEL_DO_LAGO', 'FAROL', 'PINTANGUINHA', 'PINHEIRO', 'GRUTA_DE_LOURDES', 'CANAÃ', 'SANTO_AMARO', 'JARDIM_PETRÓPOLIS', 'OURO_PRETO', 'BEBEDOURO', 'C_DE_BEBEDOURO', 'C_DE_JAQUEIRA', 'BOM_PARTO', 'PETRÓPOLIS', 'STA_AMÉLIA', 'FERNÃO_VELHO', 'RIO_NOVO', 'MUTANGE', 'JACINTINHO', 'FEITOSA', 'BARRO_DURO', 'SERRARIA', 'SÃO_JORGE', 'BENEDITO_BENTES', 'ANTARES', 'SANTOS_DUMONT', 'CLIMA_BOM', 'CIDADE_UNIVERSITÁRIA', 'SANTA_LÚCIA', 'TABULEIRO_DOS_MARTINS', 'JACARECICA', 'GARÇA_TORTA', 'CRUZ_DAS_ALMAS', 'RIACHO_DOCE', 'PESCARIA', 'IPIOCA', name='bairro'), nullable=False),
    sa.Column('horario_expediente', sa.String(length=248), nullable=False),
    sa.Column('faixa_etaria', sa.String(length=248), nullable=False),
    sa.PrimaryKeyConstraint('idpontovacinacao')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ponto_vacinacao')
    # ### end Alembic commands ###
