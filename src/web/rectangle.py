from fastapi import APIRouter
from model.rectangle import Rectangle
import fake.rectangle as service

router = APIRouter(prefix = "/rectangle")

@router.get("/")
def get_all() -> list[Rectangle]:
    return service.get_all()

@router.get("/get")
def get_one(width: float,height: float) -> Rectangle | None:
    return service.get_one(float(width),float(height))

# all the remaining endpoints do nothing yet:
@router.post("/")
def create(rectangle: Rectangle) -> Rectangle:
    return service.create(rectangle)

@router.patch("/")
def modify(rectangle: Rectangle) -> Rectangle:
    return service.modify(rectangle)

@router.put("/")
def replace(rectangle: Rectangle) -> Rectangle:
    return service.replace(rectangle)

@router.delete("/")
def delete(width: float, height: float):
    return service.delete(width,height)

@router.get("/operate")
def perimeter(width,height):
    return service.operate(width,height)