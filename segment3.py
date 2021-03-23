from vector3 import *
from segment2 import *


class Segment3:

    # start=Vector3.zero
    # end=Vector3.zero

    def __init__(self, start=Vector3(), end=Vector3()):
        self.start = start
        self.end = end

    def __mul__(a, b):
        if isinstance(b, Segment3):
            return Segment3(a.start*b.start, a.end*b.end)
        elif isinstance(b, int) or isinstance(b, float):
            return Segment3(a.start*b, a.end*b)

    #def __mul__(a, b: float): return Segment3(a.start*b, a.end*b)

    # def __truediv__(a, b):
    #     if isinstance(b, tuple):
    #         return Segment3(a.start/b[0], a.end*b[1])

    def toVector(a):
        return a.end-a.start

    def toStartAndVector(a):
        return a.start, a.toVector

    def sqrLength(a):
        return a.toVector().sqrModule()

    def length(a):
        return a.toVector().module()

    def pointOnSegment(a, t):  # t between 0 and 1
        return a.start*t+a.end*(1-t)

    def middle(a):
        return a.pointOnSegment(.5)

    def toSegment2(a):
        return Segment2(a.start.toVector2(), a.end.toVector2())

    def __str__(self):
        return "Segment3 from " + str(self.start)+" to "+str(self.end)
