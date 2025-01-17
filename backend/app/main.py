import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from api.base import api_router

from fastapi import FastAPI

def start_application():
    app = FastAPI(title = "Investment App", version="beta")
    app.include_router(api_router)
    return app

app = start_application()
