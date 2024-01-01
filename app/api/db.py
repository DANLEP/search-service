import os

from databases import Database
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DECIMAL, DateTime, ForeignKey

load_dotenv()

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

attraction = Table(
    'attraction',
    metadata,
    Column('id_attraction', Integer, primary_key=True),
    Column('name', String(50), nullable=False),
    Column('latitude', DECIMAL(8, 6), nullable=False),
    Column('longitude', DECIMAL(9, 6), nullable=False),
    Column('rating', DECIMAL(2, 1)),
)

photo = Table(
    'photo',
    metadata,
    Column('id_photo', Integer, primary_key=True),
    Column('url', String(255), nullable=False),
    Column('created_at', DateTime, nullable=False),
    Column('fk_attraction', Integer, ForeignKey('attraction.id_attraction'))
)

database = Database(DATABASE_URI)
