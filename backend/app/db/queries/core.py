# Файл с описанием функций (методов) для создания запросов и команд базе данных

import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from db.models import metadata_obj
from db.database import sync_engine

def create_tables():
    metadata_obj.create_all(sync_engine)