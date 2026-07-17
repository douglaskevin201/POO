from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Produto(Base):
    """Modelo que representa a tabela produtos"""
    # Nome da tabela no banco
    __tablename__ = 'produtos'

    # Colunas
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    descricao = Column(String(500))
    codigo = Column(String(20), unique=False, nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, default=0)

# Representação em String (opcional, mas recomendado)
def __repr__(self):
    return f"<produto(id={self.id}, nome='{self.nome}', preco={self.preco})>"