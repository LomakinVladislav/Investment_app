from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from db.config import settings

async_engine = create_async_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
)

async_session_factory = async_sessionmaker(async_engine)

async def get_session():
    async with async_session_factory() as session:
        yield session

class Base(DeclarativeBase):
    pass