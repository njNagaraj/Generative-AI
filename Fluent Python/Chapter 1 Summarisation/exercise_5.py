#demonstrating how we can overload operators using vector
import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Vector({self.x!r}, {self.y!r})'
    
    def __abs__(self):
        return math.hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2) # will call __add__() will return Vector(4, 5)
v = Vector(3, 4)
print(abs(v)) # # will call __abs__() will return 5.0
print(v * 3) # # will call __mul__() will return Vector(9, 12)
print(abs(v * 3)) # 15.0

v3 = Vector(0, 0)
print(bool(v1))  # # will call __bool__() will return Output: True
print(bool(v3))  # Output: False
