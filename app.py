from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello Samrat Soni"
    }

@app.get("/user")
def get_user():

    data = {
        "id": 1,
        "name": "Samrat"
    }
    return data