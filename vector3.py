import numpy as np

from vector2 import *


class Vector3:

    # x = 0
    # y = 0
    # z = 0

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(a, b): return Vector3(a.x+b.x, a.y+b.y, a.z+b.z)
    def __neg__(a): return Vector3(-a.x, -a.y, -a.z)
    def __sub__(a, b): return a+-b

    def __mul__(a, b):
        if isinstance(b, Vector3):
            return Vector3(a.x*b.x, a.y*b.y, a.z*b.z)
        elif isinstance(b, int) or isinstance(b, float):
            return Vector3(a.x*b, a.y*b, a.z*b)

    def __truediv__(a, b):
        if isinstance(b, Vector3):
            return Vector3(a.x/b.x, a.y/b.y, a.z/b.z)
        elif isinstance(b, int) or isinstance(b, float):
            return Vector3(a.x/b, a.y/b, a.z/b)

    def sqrModule(a):
        return a.x**2+a.y**2+a.z**2

    def module(a):
        return np.sqrt(a.sqrModule())

    def distance(a, b):
        return module(a-b)

    def normalized(a):
        return a/a.module()

    def dotProduct(a, b):
        return a.x*b.x+a.y*b.y+a.z*b.z

    def crossProduct(a, b):
        return Vector3(a.y*b.z-a.z*b.y, a.z*b.x-a.x*b.z, a.x*b.y-a.y*b.x)

    def toVector2(a):
        return Vector2(a.x, a.y)

    def toTuple(a):
        return (a.x, a.y, a.z)

    def __str__(self):
        return "Vector3(x = " + str(self.x)+", y = "+str(self.y)+", z = "+str(self.z)+")"


Vector3.zero = Vector3(0, 0, 0)
Vector3.one = Vector3(1, 1, 1)
Vector3.right = Vector3(1, 0, 0)
Vector3.forward = Vector3(0, 1, 0)
Vector3.up = Vector3(0, 0, 1)
Vector3.left = Vector3(-1, 0, 0)
Vector3.back = Vector3(0, -1, 0)
Vector3.down = Vector3(0, 0, -1)
