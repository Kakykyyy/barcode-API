from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ProductBase(BaseModel):
    codigo_barras: str

class ProductCreate(ProductBase):
    data_entrada: datetime

class Product(ProductBase):
    id: int
    data_entrada: datetime

    model_config = ConfigDict(from_attributes=True)
