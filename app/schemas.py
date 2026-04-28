from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProductBase(BaseModel):
    codigo_barras: str

class ProductCreate(ProductBase):
    data_entrada: Optional[datetime] = None

class Product(ProductBase):
    id: int
    data_entrada: datetime

    class Config:
        orm_mode = True