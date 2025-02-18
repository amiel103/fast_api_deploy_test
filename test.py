from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel



# Create a FastAPI application
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, DS"}


@app.get("/welcome")
def read_root():
    return {"welcome_message": "this is the welcome endpoint"}



