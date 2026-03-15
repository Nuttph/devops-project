import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

class Database:
    client: AsyncIOMotorClient = None
    db = None

db_context = Database()

async def connect_to_mongo():
    db_context.client = AsyncIOMotorClient(os.getenv("MONGODB_URL"))
    db_context.db = db_context.client[os.getenv("DB_NAME")]
    print("✅ MongoDB Connected")

async def close_mongo_connection():
    if db_context.client:
        db_context.client.close()

def get_db():
    return db_context.db