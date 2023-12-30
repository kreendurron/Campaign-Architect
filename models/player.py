from pydantic import BaseModel

class Player(BaseModel):
    name: str
    hero_points: int
