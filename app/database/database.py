
from dotenv import load_dotenv
from motor import motor_asyncio
import os

load_dotenv()

client = motor_asyncio.AsyncIOMotorClient(os.getenv('JWT_SECRET_MANGO_URL'))
db = client[os.getenv('JWT_SECRET_MANGO_COLLECTION_NAME')]
