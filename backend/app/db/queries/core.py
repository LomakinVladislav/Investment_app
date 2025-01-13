# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import text, insert
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from db.models import metadata_obj, users_table
from db.database import sync_engine

def create_tables():
    sync_engine.echo = False
    metadata_obj.drop_all(sync_engine)
    metadata_obj.create_all(sync_engine)
    sync_engine.echo = True

def insert_data():
    with sync_engine.connect() as conn:
        stmt = insert(users_table).values(
            [
                {"name": "Satoshi"},
                {"name": "Elon"}
            ]
        )
        conn.execute(stmt)
        conn.commit()