from sqlalchemy import create_engine

# SQLite em arquivo
engine = create_engine('sqlite:///meu_banco.db', echo=True)

#SQLite em memória 
engine = create_engine('sqlite:///:memory:', echo=True)

#PostgreSQL
# engine = create_engine('postgresql://usuario:senha@local/nome_banco')

# MySQL
# engine = create_engine('mysql+pymysql://usuario:senha@localhost/nome_banco')

