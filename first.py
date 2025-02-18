from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # This allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # This allows all headers
)
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None 



@app.get("/run")
def read_root():
    a = 1
    b = 2 
    c = 3
    return {"message": a+b+c}

@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"Item '{item.name}' has been created!", "item": item}
