from vector3 import *
from quaternion import *
from unit import *


class PosRotScale3:

    # position = Vector3.zero
    # rotation = Quaternion.zero
    # scale = Vector3.one

    def __init__(self, position=Vector3(), rotation=Quaternion(), scale=Vector3(1, 1, 1)):
        self.position = position
        self.rotation = rotation
        self.scale = scale

    # (pos=Vector3(), parentPos=Vector3(), parentRot=Quaternion()):
    def relativePos(pos, parentPosRotScale3):
        return parentPosRotScale3.rotation.rotatedPoint(pos*parentPosRotScale3.scale)+parentPosRotScale3.position
        # return Quaternion.rotatedPoint(parentRot, pos)+parentPos

    def relative(localPosRotScale3, parentPosRotScale3):
        parentPos, parentRot, parentScale = parentPosRotScale3.position, parentPosRotScale3.rotation, parentPosRotScale3.scale
        pos, rot, scale = localPosRotScale3.position, localPosRotScale3.rotation, localPosRotScale3.scale
        return PosRotScale3(
            PosRotScale3.relativePos(pos, parentPosRotScale3),
            rot.rotated(parentRot),  # parentRot.compose(rot),
            parentScale*scale)

    def __str__(self):
        return "PosRotScale3 of position " + str(self.position)+", rotation "+str(self.rotation)+", scale "+str(self.scale)


PosRotScale3.zero = PosRotScale3()


class Transform3Master(Unit):

    # localPosRotScale3=PosRotScale3.zero
    # children = []

    def __init__(self, localPosRotScale3=PosRotScale3(Vector3(), Quaternion(), Vector3(1, 1, 1)), children=[]):
        self.localPosRotScale3 = localPosRotScale3
        self.setChildren(children)
        # self.children = children
        # for child in self.children:
        #     child.parent = self

    def setChildren(self, newChildren):
        self.children = newChildren
        for child in self.children:
            child.parent = self

    def addChild(self, newChild):
        self.children.append(newChild)
        self.children[-1].parent = self

    def globalPosRotScale3(self): return self.localPosRotScale3

    def __str__(self):
        return "Master Transform3 with "+str(len(self.children)) + " children"


# Transform3Master.Master = Transform3Master(PosRotScale3(), [])
Transform3Master.Master = Transform3Master()


class Transform3(Transform3Master):

    # parent = Transform3.Master

    def __init__(self, localPosRotScale3=PosRotScale3(), children=[], parent=Transform3Master.Master):
        self.localPosRotScale3 = localPosRotScale3

        self.setParent(parent)
        self.setChildren(children)

    def setParent(self, newParent=Transform3Master.Master):
        #print(self, newParent)
        newParent.addChild(self)  # Transform3.addChild(newParent, self)

    def globalPosRotScale3(self):
        #print(self, self.parent)
        return self.localPosRotScale3.relative(self.parent.globalPosRotScale3())
        # parentPosRotScale3 = parent.globalPosRotScale3()
        # parentPos, parentRot, parentScale = parentPosRotScale3.position, parentPosRotScale3.rotation, parentPosRotScale3.scale
        # pos, rot, scale = localPosRotScale3.position, localPosRotScale3.rotation, localPosRotScale3.scale

        # return PosRotScale3(
        #     parentRot.rotatedPoint(pos-parentPos)+parentPos,
        #     parentRot*rot,  # parentRot.compose(rot),
        #     parentScale*scale)

    def __str__(self):
        return "Transform3 of local "+str(self.localPosRotScale3) + " with "+str(len(self.children)) + " children"
