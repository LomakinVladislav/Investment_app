from sqlalchemy import Table, Column, Integer, String, MetaData

metadata_obj = MetaData()

user_table = Table(
    "user",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("username", String)
)