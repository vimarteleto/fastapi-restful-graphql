# import requests
from fastapi import FastAPI
from routes.category_route import router as category_router

app = FastAPI()

@app.get("/", tags=["Tag"])
def home():
    return {
        "message": "Hello!"
    }


app.include_router(category_router, tags=["Category"], prefix="/category")