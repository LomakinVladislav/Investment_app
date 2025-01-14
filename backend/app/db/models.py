from typing import Annotated
import datetime
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from db.database import Base

intpk = Annotated[int, mapped_column(primary_key=True)]

class clientOrm(Base):
    __tablename__ = "client"  

    id: Mapped[intpk]
    name: Mapped[str]


class cryptocurrencyOrm(Base):
    __tablename__ = "cryptocurrency" 

    id: Mapped[intpk]
    name: Mapped[str]
    

class assetOrm(Base):
    __tablename__ = "asset" 

    client_id: Mapped[int] = mapped_column(ForeignKey("client.id", ondelete="CASCADE"), primary_key=True)
    cryptocurrency_id: Mapped[int] = mapped_column(ForeignKey("cryptocurrency.id", ondelete="CASCADE"), primary_key=True)
    quantity: Mapped[float]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc', now())"))
