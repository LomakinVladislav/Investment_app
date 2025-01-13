import asyncio
from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import Session, sessionmaker, DeclarativeBase
from sqlalchemy import String, create_engine, text

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from db.config import settings

sync_engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
    echo=True,
    # pool_size=5,
    # max_overflow=10,
)

session_factory = sessionmaker(sync_engine)

with sync_engine.connect() as conn:
    res = conn.execute(text("SELECT VERSION()"))
    print(f"{res=}")