from fastapi import APIRouter

import os
import sys
sys.path.insert(2, os.path.join(sys.path[0], '../..'))
from backend.app.clients.coinmarketcap.http_client import CMCHTTPClient
from config import settings

router = APIRouter()

cmc_client = CMCHTTPClient(
    base_url = "https://pro-api.coinmarketcap.com",
    api_key = settings.CMC_API_KEY
)

@router.get("/cryptocurrecies")
async def get_cryptocurrencies():
    return await cmc_client.get_listings()


@router.get("/cryptocurrecies/{currency_id}")
async def get_cryptocurrency(currency_id: int):
    return await cmc_client.get_currency(currency_id)