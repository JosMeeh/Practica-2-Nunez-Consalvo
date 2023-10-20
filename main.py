from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Practica 2 Jose Nunez Eduardo Consalvo"}


@app.get("/integrantes/{id}")
def show_integrantes(id):
        return {"data": id}

