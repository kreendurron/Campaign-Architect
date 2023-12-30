from fastapi import FastAPI
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from routes.players_routes import players_router
from routes.routes import router

app = FastAPI()

# Load environment variables from .env file
load_dotenv()

uri = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(uri)

# Connect "/"
app.include_router(router)


# Connect "/Players"
app.include_router(players_router)



# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)