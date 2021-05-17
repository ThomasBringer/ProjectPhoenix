from transform3 import *
# from segment3 import *
from unit import *


MeshRenderers = []


class MeshRenderer(Unit):
    def __init__(self, mesh):  # , entity, transform):
        self.mesh = mesh

    def globalPoints(self):
        return [PosRotScale3.relativePos(point, self.transform.globalPosRotScale3()) for point in self.mesh.points]

    def __str__(self):
        return "Renderer of " + str(self.mesh)
