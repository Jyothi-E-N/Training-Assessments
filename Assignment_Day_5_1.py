# Assignemnt 5.1
# Create a Model for representing Circle Object
# It should have
#   radius
#   area
#   perimeter
#   info
#   draw

from math import sqrt

class Circle:
   pass

def create(radius):
   c=Circle()
   c.radius = radius
   return c

def is_valid(c):
    return isinstance(c, Circle) and c.radius>0

def perimeter(c):
   return (2 * 3.14 * c.radius) if is_valid(c) else float('nan')

def area(c):
   return 3.14 * (c.radius ** 2) if is_valid(c) else fload('nan')

def info(c):
   return f'Circle<{c.radius}>' if is_valid(c) else '<Invalid Circle>'

def draw(c):
   print(info(c))


def test_circle(r):
    c = create(r)
    draw(c)
    if(is_valid(c)):
        print(f'Area={area(c)}')
        print(f'Perimeter={area(c)}')

test_circle(3)
