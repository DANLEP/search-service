from fastapi import APIRouter

search = APIRouter()


@search.get("/")
async def search_query(search_param: str):
    return {"detail": "Hello World"}
