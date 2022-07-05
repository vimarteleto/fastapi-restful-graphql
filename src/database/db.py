import motor.motor_asyncio

MONGO_DETAILS = "mongodb://irroba:irr157ba@mongo:27017/"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.irroba

category_collection = database.get_collection("category_collection")

