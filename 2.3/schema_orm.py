from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Passo 1: criar a engine de conexão ao banco de dados SQLite
# "sqlite:///meu_banco.db" -> cria/usa o arquivo meu_banco.db na mesma pasta do script
# echo=True -> mostra no console todo o SQL que o SQLAlchemy está executando por baixo dos panos
engine = create_engine("sqlite:///meu_banco.db", echo=True)

# Passo 2: criar a base declarativa
# Toda classe que representa uma tabela do banco vai herdar dessa Base
Base = declarative_base()

# Passo 3: definir a classe Cliente, que representa a tabela "clientes"
class Cliente(Base):
    __tablename__ = 'clientes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True)  # unique=True -> não pode haver dois clientes com o mesmo email
    telefone = Column(String)

# Passo 4: criar a tabela no banco de dados, caso ela ainda não exista
Base.metadata.create_all(engine)

# Passo 5: criar uma sessão para manipulação de dados
# A Session é o que o SQLAlchemy usa para conversar com o banco (parecido com o "cursor" do sqlite3 puro)
Session = sessionmaker(bind=engine)
session = Session()

# Passo 6: inserir um novo cliente (equivalente ao INSERT do SQLite)
# Antes de inserir, verificamos se já existe um cliente com esse email,
# já que a coluna email é unique=True. Sem essa checagem, rodar o script
# mais de uma vez causaria o erro: UNIQUE constraint failed: clientes.email
cliente_existente = session.query(Cliente).filter_by(email='maria@email.com').first()

if not cliente_existente:
    novo_cliente = Cliente(nome='Maria Oliveira', email='maria@email.com', telefone='11987654321')
    session.add(novo_cliente)
    session.commit()
    print("Cliente inserido com sucesso.")
else:
    print("Cliente já existe no banco, inserção não realizada.")

# Passo 7: consultar os clientes (equivalente ao SELECT * FROM clientes)
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(cliente.id, cliente.nome, cliente.email, cliente.telefone)

# Passo 8: encerrar a sessão
session.close()