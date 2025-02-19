from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import csv



# Create a FastAPI application
app = FastAPI()

class User(BaseModel):
    id:float
    name: str
 

@app.get("/get_all_data")
def read_root():

    csv_content = []
    with open('my_file.csv', mode='r', newline='') as file:
        csvreader = csv.reader(file)
        next(csvreader)
        for x in csvreader:
            csv_content.append(x)
    return {"content": csv_content}


@app.post("/add_user/")
async def create_item(user: User):

    with open('my_file.csv', mode='a',newline='') as file:
        csvwriter = csv.writer(file)

        csvwriter.writerow([user.id, user.name])


    return {"message": f"Item '{user.name}' has been created!", "item": user}

@app.get("/welcome")
def read_root():
    return {"welcome_message": "this is the welcome endpoint"}


@app.get("/hello")
def read_root():
    return {"hello": "hello there"}



