# players_route.py
from fastapi import APIRouter, HTTPException
from models.player import Player  # assuming your Pydantic model is defined here
from config.database import players_collection  # assuming you have a MongoDB collection setup
from schema.schemas import serialize_player, serialize_players  # your serialization functions
from bson import ObjectId

players_router = APIRouter()

@players_router.get("/players")
async def get_all_players():
    players = players_collection.find()
    return serialize_players(players)

@players_router.get("/players/{player_id}")
async def get_player(player_id: str):
    if not ObjectId.is_valid(player_id):
        raise HTTPException(status_code=400, detail=f"Invalid player ID: {player_id}")

    player = players_collection.find_one({"_id": ObjectId(player_id)})
    if player is not None:
        return serialize_player(player)
    else:
        raise HTTPException(status_code=404, detail=f"Player not found with ID: {player_id}")

@players_router.post("/players", response_model=Player)
async def create_player(player: Player):
    new_player = players_collection.insert_one(player.dict())
    created_player = players_collection.find_one({"_id": new_player.inserted_id})
    return serialize_player(created_player)

@players_router.put("/players/{player_id}", response_model=Player)
async def update_player(player_id: str, updated_player: Player):
    if not ObjectId.is_valid(player_id):
        raise HTTPException(status_code=400, detail=f"Invalid player ID: {player_id}")

    players_collection.update_one({"_id": ObjectId(player_id)}, {"$set": updated_player.dict()})
    player = players_collection.find_one({"_id": ObjectId(player_id)})
    if player is not None:
        return serialize_player(player)
    else:
        raise HTTPException(status_code=404, detail=f"Player not found with ID: {player_id}")

@players_router.delete("/players/{player_id}")
async def delete_player(player_id: str):
    if not ObjectId.is_valid(player_id):
        raise HTTPException(status_code=400, detail=f"Invalid player ID: {player_id}")

    result = players_collection.delete_one({"_id": ObjectId(player_id)})
    if result.deleted_count:
        return {"status": "success", "detail": f"Player with ID: {player_id} deleted."}
    else:
        raise HTTPException(status_code=404, detail=f"Player not found with ID: {player_id}")
