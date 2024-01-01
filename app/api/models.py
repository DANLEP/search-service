from datetime import datetime
from typing import Optional, List

from pydantic import BaseModel


class Photo(BaseModel):
    url: str
    id_photo: int
    created_at: datetime


class AttractionPreview(BaseModel):
    id_attraction: int
    name: str
    latitude: float
    longitude: float
    rating: Optional[float]
    review_count: Optional[int]
    like_count: Optional[int]
    photos: Optional[List[Photo]]
