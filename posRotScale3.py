from space import *
from unit import *


class PosRotScale3:

    def __init__(self, position=Vector3(), rotation=Quaternion(), scale=Vector3(1, 1, 1)):
        self.position = position
        self.rotation = rotation
        self.scale = scale

    def relativePos(pos, parentPosRotScale3):
        return parentPosRotScale3.rotation.rotatedPoint(pos * parentPosRotScale3.scale) + parentPosRotScale3.position

    def relative(localPosRotScale3, parentPosRotScale3):
        parentPos, parentRot, parentScale = parentPosRotScale3.position, parentPosRotScale3.rotation, parentPosRotScale3.scale
        pos, rot, scale = localPosRotScale3.position, localPosRotScale3.rotation, localPosRotScale3.scale
        return PosRotScale3(
            PosRotScale3.relativePos(pos, parentPosRotScale3),
            rot.rotated(parentRot),
            parentScale * scale)

    def translate(self, pos):
        self.position += pos

    def rotate(self, rot):
        self.rotation = self.rotation.rotated(rot)

    def scalate(self, scale):
        self.scale *= scale

    def transRotScalate(self, posRotScale3):
        self.translate(posRotScale3.position)
        self.rotate(posRotScale3.rotation)
        self.scalate(posRotScale3.scale)

    def __str__(self):
        return "PosRotScale3 of position " + str(self.position) + ", rotation " + str(self.rotation) + ", scale " + str(self.scale)


PosRotScale3.zero = PosRotScale3()
