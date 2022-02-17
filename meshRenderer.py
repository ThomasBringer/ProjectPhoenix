from transform3 import *
# from segment3 import *
from unit import *
from color import *

MeshRenderers = []


class MeshRenderer(Unit):
    # , entity, transform):
    def __init__(self, mesh, segColor=Color.black, triColor=Color.grey):
        self.mesh = mesh
        self.segColor = segColor
        self.triColor = triColor

    def globalPoints(self):
        return [PosRotScale3.relativePos(point, self.transform.globalPosRotScale3) for point in self.mesh.points]

    def __str__(self):
        return "Renderer of " + str(self.mesh)
