# An Entity is an object that represent any actor in the project.
# Entities can represent physical objects in the scene (a roller coaster cart) or non-physical ones (a virtual camera).
# Entities do not have any functionality attached by default.
# Instead, Entities can be given functionality through Units, which provides them with specific behaviours.
# An Entity must have a Transform3 Unit attached, which means that an entity must be placed in the scene.

from transform3 import *
from mesh import *
from unit import *
from camera import *
from bezier3 import*
from track import *
from trackIntegrator import TrackIntegrator
from trackMesh import *
from trackBody import *
from meshRenderer import *
from vectorRenderer import *


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
            if isinstance(unit, VectorRenderer):
                VectorRenderers.append(unit)
            if isinstance(unit, UpdatableUnit):
                UpdatableUnits.append(unit)

    def __str__(self):
        return "Entity with transform " + str(self.transform) + " and units: " + str([str(u) for u in self.units])
