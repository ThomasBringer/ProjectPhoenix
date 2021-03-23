from vector2 import *
from vector3 import *
from segment import *


class Segment2(Segment):

    def __init__(self, start=Vector2(), end=Vector2()):
        self.start = start
        self.end = end

    def __str__(self):
        return "Segment2 from "+str(self.start)+" to "+str(self.end)
