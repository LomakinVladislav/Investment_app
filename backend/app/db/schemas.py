from datetime import datetime
from pydantic import BaseModel

class ClientAddSchema(BaseModel):
    name: str
    country: str

class ClientSchema(ClientAddSchema):
    id: int

class cryptocurrencyAddSchema(BaseModel):
    name: str

class cryptocurrencySchema(cryptocurrencyAddSchema):
    id: int

class assetAddShema(BaseModel):
    client_id: int
    cryptocurrency_id: int
    quantity: float
    price: float
    # created_at: datetime

class assetShema(assetAddShema):
    id: int

