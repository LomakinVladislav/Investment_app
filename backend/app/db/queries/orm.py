# Файл с описанием функций (методов) для создания запросов и команд базе данных
from sqlalchemy import text, insert
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from db.models import assetOrm, clientOrm, cryptocurrencyOrm
from db.database import Base, sync_engine, session_factory

def create_tables():
    sync_engine.echo=True
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)

def insert_data():
    with session_factory() as session:
        user1 = clientOrm(name="John")
        user2 = clientOrm(name="James")
        crypto1 = cryptocurrencyOrm(name="Ethereum")
        session.add_all([user1, user2, crypto1])
        session.commit()
        asset1 = assetOrm(client_id="1", cryptocurrency_id="1", quantity="0.5")
        session.add_all([asset1])
        session.commit()