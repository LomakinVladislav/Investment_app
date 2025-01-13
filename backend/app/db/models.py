from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata_obj = MetaData()

users_table = Table(
    "users",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)

assets_table = Table(
    "assets",
    metadata_obj,
    Column("user_id", Integer, ForeignKey('users.id'), primary_key=True),
    Column("currency_id", Integer, ForeignKey('cryptocurrencies.id'), primary_key=True),
)

cryptocurrencies_table = Table(
    "cryptocurrencies",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("name", String),
)