from fastapi import FastAPI;
from pymongo import MongoClient;
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
uri = os.getenv("MONGODB_URI")

client = MongoClient(uri)

db = client.dnd

COL_CHARACTERS = db["CHARACTERS"]