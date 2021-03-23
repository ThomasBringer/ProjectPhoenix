from transform3 import *
from mesh import *
from unit import *
from camera import *


class Entity:

    def __init__(self, transform=Transform3Master.Master, units=[]):
        transform.entity = self
        self.transform = transform
        self.units = units
        for unit in self.units:
            unit.transform = transform
            unit.entity = self
            if type(unit) == Mesh:
                Meshes.append(unit)

    def __str__(self):
        return "Entity with transform "+str(self.transform) + " and units: "+str([str(u) for u in self.units])


boxTrans = Transform3(PosRotScale3(
    Vector3(0, 0, 0), Quaternion(), Vector3(1, 1, 1)), [], Transform3Master.Master)
Box = Entity(boxTrans, [Mesh.Box])
Pyramid = Entity(Transform3(PosRotScale3(
    Vector3.up*.5, Quaternion(), Vector3.one*.5), [], boxTrans), [Mesh.Pyramid])
MainCamera = Entity(Transform3(PosRotScale3(Vector3(0, 0, 0))), [Camera.Main])
