# Core do SQLAlchemy 
from sqlalchemy import create_engine, column, Integer, String, Float, Date, Boolean, Text

# Declarative Base (para definir modelos)
from sqlalchemy.ext.declarative import declarative_base

# Session para (interagir com o banco)
from sqlalchemy.orm import sessionmaker, Session

# Tipos de dados adicionais 
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship

# Para datas 
from datetime import datetime, date
