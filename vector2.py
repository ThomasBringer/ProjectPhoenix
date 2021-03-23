import numpy as np


class Vector2:

    # x = 0
    # y = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(a, b): return Vector2(a.x+b.x, a.y+b.y)
    #def __sub__(a, b): return Vector2(a.x-b.x, a.y-b.y)
    def __neg__(a): return Vector2(-a.x, -a.y)
    def __sub__(a, b): return a+-b

    def __mul__(a, b):
        if isinstance(b, Vector2):
            return Vector2(a.x*b.x, a.y*b.y)
        elif isinstance(b, int) or isinstance(b, float):
            return Vector2(a.x*b, a.y*b)

    def __truediv__(a, b):
        if isinstance(b, Vector2):
            return Vector2(a.x/b.x, a.y/b.y)
        elif isinstance(b, int) or isinstance(b, float):
            return Vector2(a.x/b, a.y/b)

    # def __mul__(a, b): return Vector2(a.x*b.x, a.y*b.y)
    # def __truediv__(a, b): return Vector2(a.x/b.x, a.y/b.y)

    #def __mul__(a, b: float): return Vector2(a.x*b, a.y*b)
    #def __truediv__(a, b: float): return Vector2(a.x/b, a.y/b)

    def sqrModule(a):
        return a.x**2+a.y**2

    def module(a):
        return np.sqrt(a.sqrModule())

    def distance(a, b):
        return module(a-b)

    def normalized(a):
        return a/a.module()

    def toVector3(a):
        return Vector3(a.x, a.y, 0)

    def toTuple(a):
        return (a.x, a.y)

    def __str__(self):
        return "Vector2(x = " + str(self.x)+", y = "+str(self.y)+")"


Vector2.zero = Vector2(0, 0)
Vector2.one = Vector2(1, 1)
Vector2.right = Vector2(1, 0)
Vector2.forward = Vector2(0, 1)
Vector2.left = Vector2(-1, 0)
Vector2.back = Vector2(0, -1)
