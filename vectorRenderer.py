from os import startfile
from transform3 import *
# from segment3 import *
from unit import *
from color import *

VectorRenderers = []


class VectorRenderer(Unit):
    # , entity, transform):
    def __init__(self, color=Color.yellow, scale=.25, vector=Vector3()):
        self.vector = vector
        self.color = color
        self.scale = scale

    @property
    def vectorPoints(self):
        # print("rendering", self)

        start = self.transform.globalPosRotScale3.position
        # print("hey")
        # print(start)
        # print(self.vector)
        # print(start+self.vector)

        # print("vect", self.vector)

        return [start, start+PosRotScale3.relativePos(self.vector, Transform3Master.Master.globalPosRotScale3)*self.scale]

    def __str__(self):
        return "Renderer of " + str(self.vector)
