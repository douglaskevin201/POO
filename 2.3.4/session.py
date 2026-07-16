from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('sqlite:///meu_banco.db', echo=True)

# Criar uma fabrica de sessões
Session = sessionmaker(bind=engine)

# Criar uma sessão 
session = Session()

# Usar a sessão
#...opreções...

# Fechar sessão
session.close()

