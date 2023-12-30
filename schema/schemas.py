def serialize_player(player_document) -> dict:
    return {
        "id": str(player_document["_id"]),
        "name": player_document["name"],
        "hero_points": player_document["hero_points"]
    }

def serialize_players(player_documents) -> list:
    return[serialize_player(player_document) for player_document in player_documents]