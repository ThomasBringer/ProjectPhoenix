from vector2 import *
from vector3 import *
from segment3 import *


class Segment:

    def __init__(self, start=Vector(), end=Vector()):
        self.start = start
        self.end = end

    def __mul__(a, b):
        if isinstance(b, Segment):
            return Segment(a.start*b.start, a.end*b.end)
        elif isinstance(b, float) or isinstance(b, int):
            return Segment(a.start*b, a.end*b)
        elif isinstance(b, tuple):
            return Segment(a.start*b[0], a.end*b[1])

    def toVector(a):
        return a.end-a.start

    def toStartAndVector(a):
        return a.start, a.toVector()

    def sqrLength(a):
        return a.toVector().sqrModule()

    def length(a):
        return a.toVector().module()

    def pointOnSegment(a, t):  # t between 0 and 1
        return a.start*t+a.end*(1-t)

    def middle(a):
        return a.pointOnSegment(.5)

    def toSegment2(a):
        return Segment(a.start.toVector2(), a.end.toVector2())

    def toSegment3(a):
        return Segment(a.start.toVector3(), a.end.toVector3())

    def __str__(self):
        return "Segment from "+str(self.start)+" to "+str(self.end)
