
from backend.app.api.base import api_router

from fastapi import FastAPI

def start_application():
    app = FastAPI(title = "Investment App", version="beta")
    app.include_router(api_router)
    return app

app = start_application()
