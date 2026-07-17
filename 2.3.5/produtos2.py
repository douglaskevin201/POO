from sqlalchemy import Column, Integer, Float, String, CheckConstraint, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Prduto(Base):
    """Modelo que representa a tabela de produtos"""
    # Nome da tabela no banco
    __tablename__ = 'produtos'

    # Colunas (atributos)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(500))

    # 1. Constraint de coluna (NOT NULL e UNIQUE) 
    # "nullable=False" -> O banco não aceitará valores NULOS.
    # "unique=True" -> O banco garantirá que NENHUM outro   
    codigo = Column(String(20), unique=True, nullable=False)

    preco = Column(Float, nullable=False)
    estoque = Column(Integer, default=0)

    # Restrições em nível de tabela
    # 2. Constraint de tabela (CHECK)
    # "CHECK": uma regra que o proprio banco deve verificar.
    # Aqui, o banco garantirá que NUNCA um preco menor que zero 
    # Seja salvo no banco. E que NUNCA um estoque fique negativo.

    # 3. Constraint de Tabela (UNIQUE Múltipla)
    # Ex: Um código não pode ter o mesmo código de outro.
    # UniqueConstraint('codigo, name ='codigo_unico')

    __table_args__ = (
     CheckConstraint('preco > 0', name='preco_positivo'),
     CheckConstraint('estoque >= 0', name='estoque_nao_negativo'),
     UniqueConstraint('codigo', name='codigo_unico'), 
)

# Representação em string (opcional, mas recomendado)
def __repr__(self):
    return f"<Produto(id{self.id}, nome='{self.nome}', preco{self.preco})>"


