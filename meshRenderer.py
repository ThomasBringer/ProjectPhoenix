# A Unit used to attach a Mesh to an Entity.
# When an Entity has a MeshRenderer Unit attached, its geometry will be rendered by the Camera onto the canvas.

from transform3 import *
from unit import *
from color import *

MeshRenderers = []


class MeshRenderer(Unit):
    def __init__(self, mesh, segColor=Color.black, triColor=Color.grey):
        self.mesh = mesh
        self.segColor = segColor
        self.triColor = triColor

    # Global position of vertices in the scene.
    def globalPoints(self):
        return [PosRotScale3.relativePos(point, self.transform.globalPosRotScale3) for point in self.mesh.points]

    def __str__(self):
        return "Renderer of " + str(self.mesh)
