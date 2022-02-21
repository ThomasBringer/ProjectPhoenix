# A VectorRenderer is a Unit used to display dynamic Vector3s in the 3D scene.
# Can be used to display an acceleration vector of an object subject to physics.

from os import startfile
from transform3 import *
from unit import *
from color import *

VectorRenderers = []


class VectorRenderer(Unit):
    def __init__(self, color=Color.yellow, scale=.25, vector=Vector3()):
        self.vector = vector
        self.color = color
        self.scale = scale

    @property
    def vectorPoints(self):
        start = self.transform.globalPosRotScale3.position
        return [start, start+PosRotScale3.relativePos(self.vector, Transform3Master.Master.globalPosRotScale3)*self.scale]

    def __str__(self):
        return "Renderer of " + str(self.vector)
