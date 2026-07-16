from sqlalchemy.ext.declarative import declarative_base

# Criar a base
Base = declarative_base()

# Todos os modelos herdarão desta base
class MeuModelo(Base):
    __tablename__ = 'minha_tabela'
    # ...


