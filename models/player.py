from pydantic import BaseModel

class Player(BaseModel):
    name: str = "Unknown Player"
    hero_points: int = 0

    class Config:
        extra = "allow" # Allows additional dynamic fields
