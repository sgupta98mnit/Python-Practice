from math import hypot

class Vector:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __repr__(self):
        # !r calls the __repr__ method which is more accurate than !s(__str__)
        return f"Vector({self.x!r}, {self.y!r})"
        # return f"Vector({self.x!s}, {self.y!s})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __bool__(self):
        return bool(self.x or self.y)

print(Vector(1, 2))
# print(Vector('1', '2'))
print(Vector(1, 2) + Vector(3, 4))
print(Vector(1, 2) * 3)
print(abs(Vector(3, 4)))

if Vector(1, 2):
    print(f"Vector has magnitude")
else:
    print("Vector has 0 magnitude")

if Vector(0, 0):
    print(f"Vector has magnitude")
else:
    print("Vector has 0 magnitude")