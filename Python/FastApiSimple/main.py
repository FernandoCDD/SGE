from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel, PositiveInt

app = FastAPI()

class User(BaseModel):
    id: int
    name: str = 'Pepe Pérez'
    fecha_alta = datetime | None
    aficiones = dict[str, PositiveInt]

@app.get("/saludo")
async def get():
    return {"mensaje": "Que tengas un maravilloso día"}

@app.post("/item/add")
async def post(user: User):
    return user
