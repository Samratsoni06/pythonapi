from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "💕💕😘😘😘 I love you Shweta 😘😘💕💕"
    }

@app.get("/user")
def get_user():

    data = {
        "id": 1,
        "name": "Samrat"
    }
    return data