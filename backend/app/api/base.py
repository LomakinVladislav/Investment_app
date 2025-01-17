from fastapi import APIRouter

from api.v1 import route

api_router = APIRouter()
api_router.include_router(route.router,prefix="", tags=["investment_route"])