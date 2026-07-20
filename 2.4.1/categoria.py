from sqlalchemy import ForeignKey, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Categoria(Base):
    __tablename__ = 'categorias'

    id = Column(Integer, Primary_key=True)
    nome = Column(String(50), nullable=False)
    produtos = relationship('produto', back_populates='categoria')

class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, Primary_Key=True)
    nome = Column(String(100), nullable=False)
    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    categoria = relationship('Categoria', back_populates='produtos')

