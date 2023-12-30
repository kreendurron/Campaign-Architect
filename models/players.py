from pydantic import BaseModel

class Players(BaseModel):
    name: str
    hero_points: int
