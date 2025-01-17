# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import select
from sqlalchemy.orm import Session
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from db.models import assetModel, clientModel, cryptocurrencyModel
from db.database import Base, async_engine
from db.schemas import ClientAddSchema


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {"ok": True}


async def add_client(data: ClientAddSchema, session: Session):
    new_client = clientModel(
        name=data.name,
        country=data.country
    )
    session.add(new_client)
    await session.commit()
    return {"ok": True}


async def get_clients(session: Session):
    query = select(clientModel)
    result = await session.execute(query)
    return result.scalars().all()
    