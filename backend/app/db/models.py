from typing import Annotated
import datetime
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]

class clientModel(Base):
    __tablename__ = "client"  

    id: Mapped[intpk]
    name: Mapped[str]
    country: Mapped[str]


class cryptocurrencyModel(Base):
    __tablename__ = "cryptocurrency" 

    id: Mapped[intpk]
    name: Mapped[str]
    

class assetModel(Base):
    __tablename__ = "asset" 

    id: Mapped[intpk]
    client_id: Mapped[int] = mapped_column(ForeignKey("client.id", ondelete="CASCADE"))
    cryptocurrency_id: Mapped[int] = mapped_column(ForeignKey("cryptocurrency.id", ondelete="CASCADE"))
    quantity: Mapped[float]
    price: Mapped[float]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
