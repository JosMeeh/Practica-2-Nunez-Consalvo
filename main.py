from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from sqlalchemy.dialects.postgresql import psycopg2


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



##Para conexion con base de datos
def conexionPostgres():
    conexion = psycopg2.connect(host="***", database="***", user="***", password="***")
    cur = conexion.cursor()
    cur.execute( "SELECT nombre, apellidos FROM empleados")
    conexion.close();




