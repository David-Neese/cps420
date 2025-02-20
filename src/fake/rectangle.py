from model.rectangle import Rectangle

# fake data, replaced in Chapter 10 by a real database and SQL
_rectangles = [
    Rectangle(width=1.0,height=2.0),
    Rectangle(width=50.0,height=5.0),
    Rectangle(width=6.6743,height=8.99),
    Rectangle(width=50.0,height=50.0),
    ]

def get_all() -> list[Rectangle]:
    return _rectangles

def get_one(width: float,height: float):
    for _rectangle in _rectangles:
        print(width)
        if float(_rectangle.width) == float(width) and float(_rectangle.height) == float(height):
            return _rectangle
    return None

def operate(width: float, height: float):
    message = "No rectangle found!"
    if(get_one(width,height) != None):
        message = "Perimeter: " + str(float(width) * 2 + float(height) * 2) + " Area: " + str(float(width) * float(height))
    return message

# The following are nonfunctional for now,
# so they just act like they work, without modifying
def create(rectangle: Rectangle) -> Rectangle:
    return rectangle

def modify(rectangle: Rectangle) -> Rectangle:
    return rectangle

def replace(rectangle: Rectangle) -> Rectangle:
    return rectangle

def delete(width: float, height: float) -> bool:
    return None
