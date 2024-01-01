import os

from dotenv import load_dotenv
from fastapi import APIRouter

from app.api import db_manager
from app.api.models import AttractionPreview, Photo

search = APIRouter()
load_dotenv()

GKS_PUBLIC_URL = os.getenv('GKS_PUBLIC_URL')
BUCKET_NAME = os.getenv('BUCKET_NAME')


@search.get("/attractions")
async def get_attractions_for_user(id_user: int):
    attractions = await db_manager.get_user_attractions_previews(id_user)
    attr_out = []
    for attraction in attractions:
        photos = await db_manager.get_attraction_photos(attraction["id_attraction"])
        photos_out = []

        for photo in photos:
            photos_out.append(
                Photo(id_photo=photo['id_photo'], created_at=photo['created_at'],
                                   url=f"{GKS_PUBLIC_URL}{BUCKET_NAME}/photo/{photo['url']}")
            )

        attr_out.append(
            AttractionPreview(**attraction, photos=photos_out)
        )
    return attr_out
