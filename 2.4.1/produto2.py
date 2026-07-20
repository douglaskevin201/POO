from sqlalchemy import Table, Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

produto_tag = Table('produto_tag', Base.metadata,
    Column('produto_id', Integer, ForeignKey('produtos.id')),
    Column('tag_id', Integer, ForeignKey('tags.id')),
    )

class Produto(Base):
    __tablenome__ = 'produtos'

    id = Column(Integer, Primary_Key=True)
    nome = Column(String(100))
    tags = relationship('Tag', secondary=produto_tag, back_populates='produtos')

class Tags(Base):
    __tablename__ = 'tags'

    id = Column(Integer, Primary_Key=True)
    nome = Column(String(30))
    produtos = relationship('produto', secondary=produto_tag, back_populates='tags')

