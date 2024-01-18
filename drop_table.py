# drop_table.py
from sqlalchemy import create_engine, MetaData
from dotenv import load_dotenv
import os
from typing import Any

load_dotenv()

SQLALCHEMY_DATABASE_URL: Any = os.getenv("DATABASE_CON_KEY")
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)

metadata = MetaData()
existing_table = metadata.tables.get("prac_todos")

print(existing_table)

print(metadata.tables.keys())


if existing_table is not None:
    existing_table.drop(engine, checkfirst=True)
    print("Existing table dropped successfully.")
else:
    print("Table does not exist.")
