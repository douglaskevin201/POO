
'''Exemplo prático que mostra como excluir uma categoria de produtos e,
ao mesmo tempo, apagar todos os produtos associados a ela no banco de dados
usando Python e a biblioteca SQLAlchemy'''

class Categoria(Base):
    __tablename__ = 'categorias'
    id = Column(Integer, primary_key=True)
    produtos = relationship('Produto',
        back_populates='categoria',
        cascade="all, delete-orphan")

categoria = session.query(Categoria).filter_by(id=1).first()
session.delete(categoria)
session.commit()