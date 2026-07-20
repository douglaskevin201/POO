from sqlalchemy import UniqueConstraint, CheckConstraint, Index
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    username = Column(String(50), nullable=False)
    idade = Column(Integer, CheckConstraint('idade >= 18'))

    __table_args__ = (
        UniqueConstraint('email', name='uq_email'),
        Index('idc_usarname', 'username'),
    )