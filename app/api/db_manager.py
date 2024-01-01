from sqlalchemy import desc

from app.api.db import photo, database
from app.api import sql_querys


async def get_attraction_photos(id_attraction: int):
    query = (photo.select(photo.c.fk_attraction == id_attraction)
             .order_by(desc(photo.c.created_at))
             .limit(3))
    return await database.fetch_all(query=query)


async def get_user_attractions_previews(id_user: int):
    query = sql_querys.get_new_attraction_preview_for_user

    return await database.fetch_all(query=query, values={"id": id_user})
