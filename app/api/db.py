import os

from databases import Database
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData

load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

database = Database(DATABASE_URI)
