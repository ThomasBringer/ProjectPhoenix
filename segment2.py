from vector2 import *
from segment3 import *


class Segment2:

    # start=Vector2.zero
    # end=Vector2.zero

    def __init__(self, start=Vector2(), end=Vector2()):
        self.start = start
        self.end = end

    # def __mul__(a, b):
    #     # if isinstance(b, Segment2):
    #     #     return Segment2(a.start*b.start, a.end*b.end)
    #     if isinstance(b, float) or isinstance(b, int):
    #         return Segment2(a.start*b, a.end*b)
    #     # elif isinstance(b, tuple):
    #     #     return Segment2(a.start/b[0], a.end*b[1])

    def __mul__(a, b):
        if isinstance(b, Segment2):
            return Segment2(a.start*b.start, a.end*b.end)
        elif isinstance(b, float) or isinstance(b, int):
            return Segment2(a.start*b, a.end*b)
        elif isinstance(b, tuple):
            return Segment2(a.start*b[0], a.end*b[1])

    # def __truediv__(a, b):
    #     if isinstance(b, tuple):
    #         return Segment2(a.start/b[0], a.end*b[1])

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

    def toSegment3(a):
        return Segment3(a.start.toVector3(), a.end.toVector3())

    def __str__(self):
        return "Segment2 from "+str(self.start)+" to "+str(self.end)
