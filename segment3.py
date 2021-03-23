from vector3 import *
from segment import *


class Segment3(Segment):

    def __init__(self, start=Vector3(), end=Vector3()):
        self.start = start
        self.end = end

    def __str__(self):
        return "Segment3 from " + str(self.start)+" to "+str(self.end)
