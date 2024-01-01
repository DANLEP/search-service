from fastapi import FastAPI

from app.api.db import metadata, engine, database
from app.api.search import search

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/search/openapi.json", docs_url="/api/v1/search/docs")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(search, prefix='/api/v1/search', tags=['search'])
