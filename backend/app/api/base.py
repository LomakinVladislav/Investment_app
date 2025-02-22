from fastapi import APIRouter

from backend.app.api.v1 import route
from backend.app.api.v1 import route_CMC

api_router = APIRouter()
api_router.include_router(route.router,prefix="", tags=["Database_route"])
api_router.include_router(route_CMC.router,prefix="", tags=["CoinMarketCap_route"])