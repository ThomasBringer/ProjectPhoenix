from transform3 import *
from mesh import *
from unit import *
from camera import *
from track import *
from trackMesh import *
from trackBody import *
from meshRenderer import *


class Entity:

    def __init__(self, transform=Transform3(), units=[]):
        transform.entity = self
        self.transform = transform
        self.units = units
        for unit in self.units:
            unit.transform = transform
            unit.entity = self
            if isinstance(unit, MeshRenderer):
                MeshRenderers.append(unit)
            if isinstance(unit, UpdatableUnit):
                UpdatableUnits.append(unit)

    def __str__(self):
        return "Entity with transform " + str(self.transform) + " and units: " + str([str(u) for u in self.units])


# boxTrans = Transform3(PosRotScale3(
#     Vector3(0, 0, 0), Quaternion(), Vector3(1, 1, 1)), [], Transform3Master.Master)
# Box = Entity(boxTrans, [MeshRenderer(Mesh.Cube)])
# Pyramid = Entity(Transform3(PosRotScale3(
#     Vector3.up * .5, Quaternion(), Vector3.one * .5), [], boxTrans), [MeshRenderer(Mesh.Pyramid)])
# selectedEntity = Pyramid

Ground = Entity(Transform3(PosRotScale3(Vector3(0, 0, -5))),
                [MeshRenderer(Mesh.Ground)])
Ground.transform.localPosRotScale3.scale = Vector3.one * 3
Cart = Entity(Transform3(PosRotScale3(
    Track.T01.start, Quaternion(), Vector3(1, 1, 1)), [], Transform3Master.Master), [MeshRenderer(Mesh.Cart), TrackBody(Track.T01)])
Track01 = Entity(Transform3(PosRotScale3(
    Vector3(0, 0, 0), Quaternion(), Vector3(1, 1, 1)), [], Transform3Master.Master), [MeshRenderer(TrackMesh(Track.T01))])
selectedEntity = Cart

MainCamera = Entity(Transform3(PosRotScale3(Vector3(0, 0, 0))), [Camera.Main])

#########################
# Pyramid = Entity(Transform3(PosRotScale3(Vector3.up * .5, Quaternion(),
#                                          Vector3.one * .5), [], Cart.transform), [MeshRenderer(Mesh.Pyramid)])

# Box1 = Entity(Transform3(PosRotScale3(Vector3(2, 2, 0))),
#               [MeshRenderer(Mesh.Cube)])
# Box2 = Entity(Transform3(PosRotScale3(Vector3(2, -2, 0))),
#               [MeshRenderer(Mesh.Cube)])
# Box3 = Entity(Transform3(PosRotScale3(Vector3(-2, 2, 0))),
#               [MeshRenderer(Mesh.Cube)])
# Box4 = Entity(Transform3(PosRotScale3(Vector3(-2, -2, 0))),
#               [MeshRenderer(Mesh.Cube)])

# MainCamera = Entity(Transform3(PosRotScale3(
#     Vector3(0, 0, 0)), [], Cart.transform), [Camera.Main])
