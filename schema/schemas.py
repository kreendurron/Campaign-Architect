def serialize_player(player_document) -> dict:
    """
    Serialize a single player document from MongoDB to a dictionary format.

    Args:
    player_document (dict): A dictionary representing a player document from MongoDB.

    Returns:
    dict: A serialized player dictionary with default values for expected fields and inclusion of additional fields.
    """
    # Initialize a dictionary with default values for the expected fields.
    # Convert the MongoDB ObjectId to a string for the 'id' field.
    player_data = {
        "id": str(player_document["_id"]),
        "name": player_document.get("name", "Unknown Name"),  # Use 'Unknown Name' if 'name' is not in the document.
        "hero_points": player_document.get("hero_points", 0)   # Use 0 if 'hero_points' is not in the document.
    }

    # Add all other fields present in the MongoDB document to the serialized data.
    # This allows dynamic properties to be included.
    for key, value in player_document.items():
        if key not in ["_id", "name", "hero_points"]:
            player_data[key] = value

    return player_data


def serialize_players(player_documents) -> list:
    """
    Serialize a list of player documents from MongoDB.

    Args:
    player_documents (iterable): An iterable of MongoDB player documents.

    Returns:
    list: A list of serialized player dictionaries.
    """
    # Apply serialize_player to each document in the player_documents iterable.
    # This creates a list of serialized player dictionaries.
    return [serialize_player(player_document) for player_document in player_documents]
