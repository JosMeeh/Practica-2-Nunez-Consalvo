from fastapi import FastAPI
from pydantic import BaseModel
from typing import List



class item (BaseModel):
    id: int
    name: str
    emails: List[str]

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Practica 2 Jose Nunez Eduardo Consalvo"}


@app.get("/directory/{id}")
def show_integrantes(id):
        return {"data": id}



@app.post("/directory")
def add_directory(item: item):
 return {"Id": item.id, "Name": item.name, "Email": item.emails}



