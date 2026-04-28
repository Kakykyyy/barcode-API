from sqlalchemy import Column, Integer, String, DateTime
from .database import Base 
class Product(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, index=True)
    codigo_barras = Column(String, unique=True, index=True, nullable=False)
    data_entrada = Column(DateTime, nullable=False)