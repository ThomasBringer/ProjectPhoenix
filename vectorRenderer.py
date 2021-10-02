from os import startfile
from transform3 import *
# from segment3 import *
from unit import *
from color import *

VectorRenderers = []


class VectorRenderer(Unit):
    # , entity, transform):
    def __init__(self, color=Color.yellow, vector=Vector3()):
        self.vector = vector
        self.color = color

    @property
    def vectorPoints(self):
        start = self.transform.globalPosRotScale3.position
        # print("hey")
        # print(start)
        # print(self.vector)
        # print(start+self.vector)
        return [start, start+PosRotScale3.relativePos(
                self.vector, Transform3Master.Master.globalPosRotScale3)]

    def __str__(self):
        return "Renderer of " + str(self.vector)
