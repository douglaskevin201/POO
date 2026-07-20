from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


Base = declarative_base()

class Produto(Base):

    __tablename__ = 'produtos' #definindo nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, default=0)
    data_cadastro = Column(DateTime, default=datetime.now)

    def __repr__(self):
        #funcao que gera uma descricao simples do produto
        return f"<Produto(id={self.id}, nome='{self.nome}', preco={self.preco})"
    
