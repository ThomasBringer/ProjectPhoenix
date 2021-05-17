import numpy as np
from utilities import *


class Vector(object):

    def __init__(self, c=[0, 0]):
        self.c = c

    # @property
    # def dim(self): return len(self.c)

    @property
    def x(self): return self.c[0]

    @x.setter
    def x(self, value): self.c[0] = value

    @property
    def y(self): return self.c[1]

    @y.setter
    def y(self, value): self.c[1] = value

    @property
    def z(self): return self.c[2]

    @z.setter
    def z(self, value): self.c[2] = value

    def __add__(a, b): return Vector(sumByTerm([a.c, b.c]))
    def __neg__(a): return Vector(multTerms(-1, a.c))
    def __sub__(a, b): return a + -b

    def __mul__(a, b):
        if isinstance(b, Vector):
            return Vector(multByTerm([a.c, b.c]))
        elif isinstance(b, int) or isinstance(b, float):
            return Vector(multTerms(b, a.c))

    def __truediv__(a, b):
        if isinstance(b, Vector):
            return Vector(multByTerm([a.c, invTerms(b.c)]))
        elif isinstance(b, int) or isinstance(b, float):
            return Vector(multTerms(1 / b, a.c))

    def __eq__(a, b):
        return a.c == b.c

    def __ne__(a, b):
        return not a == b

    @property
    def sqrModule(a):
        return sum([k**2 for k in a.c])

    @property
    def module(a):
        return np.sqrt(a.sqrModule)

    # def distance(a, b):
    #     return module(a-b)

    @property
    def normalized(a):
        return a / a.module

    def toVector2(a):
        return Vector([a.x, a.y])

    def toVector3(a):
        return Vector([a.x, a.y, 0])

    def toTuple(self):
        return tuple(self.c)

    def __str__(self):
        return "Vector of coordinates(" + str([str(k) for k in self.c]) + ")"
