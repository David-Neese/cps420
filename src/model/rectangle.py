from pydantic import BaseModel

class Rectangle(BaseModel):
    width: float
    height: float