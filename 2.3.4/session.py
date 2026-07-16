from sqlalchemy.orm import sessionmaker

# Criar uma fabrica de sessões
Session = sessionmaker(bind=engine)

# Criar uma sessão 
session = Session()

# Usar a sessão
#...opreções...

# Fechar sessão
session.close()

