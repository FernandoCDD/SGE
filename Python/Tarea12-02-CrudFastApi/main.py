from fastapi import FastAPI, HTTPException, status, Query, Response
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

# Cambiar el diccionario por un List de coches.
class Car(BaseModel):
    brand: str
    model: str
    available: bool = True
    ratings: Optional[int] = None

"""
my_cars = [
    {"brand": "Toyota", "model": "Auris", "id": 1},
    {"brand": "Seat", "model": "León", "id": 2},
    {"brand": "Opel", "model": "Corsa", "id": 3},
]
"""

@app.get("/cars")
def getAllCars():
    return {"data": my_cars}


@app.post("/cars/add", status_code=status.HTTP_201_CREATED)
def add_car(car: Car):
    car_dict = car.dict()
    car_dict["id"] = randrange(0, 100000)
    my_cars.append(car_dict)
    return {"data": car_dict}


@app.get("/cars/latest")
def get_latest_car():
    car = my_cars[-1]
    return {"car_detail": car}


def find_index_car(id):
    for i, car in enumerate(my_cars):
        if car['id'] == id:
            return i

def find_car(id):
    for car in my_cars:
        if car["id"] == id:
            return car


@app.delete("/cars/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_car(id: int):
    index = find_index_car(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Car with ID: {id} doesn´t exists")

    my_cars.pop(index)
    return {"message": f"Car with ID {id} successfully deleted"}


@app.put("/cars/update/{id}")
def update_car(id: int, car: Car):
    index = find_index_car(id)
    if index is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Car with ID {id} doesn`t exists.")

    car_dict = car.dict()
    car_dict['id'] = id
    my_cars[index] = car_dict
    return {"message": f"Car with ID {id} successfully updated"}
