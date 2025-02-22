from fastapi import APIRouter, Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.db.orm import create_tables, add_client, get_clients
from backend.app.db.schemas import ClientAddSchema
from backend.app.db.database import get_session

SessionDep = Annotated[AsyncSession, Depends(get_session)]

router = APIRouter()

@router.post("/create_tables")
async def create_tables_api():
    result = await create_tables()
    return result

@router.post("/add_client")
async def add_client_api(data: ClientAddSchema, session: SessionDep):
    result = await add_client(data=data, session=session)
    return result

@router.get("/get_clients")
async def get_clients_api(session: SessionDep):
    result = await get_clients(session=session)
    return result