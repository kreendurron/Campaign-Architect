# players_routes.py
from fastapi import APIRouter, HTTPException
from models.player import Player  # assuming your Pydantic model is defined here
from config.database import players_collection  # assuming you have a MongoDB collection setup
from schema.schemas import serialize_player, serialize_players  # your serialization functions

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the D&D Campaign Management API!"}
