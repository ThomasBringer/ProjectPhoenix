from posRotScale3 import *


class Transform3Master(Unit):

    def __init__(self, localPosRotScale3=PosRotScale3(Vector3(), Quaternion(), Vector3(1, 1, 1)), children=[]):
        self.localPosRotScale3 = localPosRotScale3
        self.setChildren(children)

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


Transform3Master.Master = Transform3Master()


class Transform3(Transform3Master):

    def __init__(self, localPosRotScale3=PosRotScale3(), children=[], parent=Transform3Master.Master):
        self.localPosRotScale3 = localPosRotScale3
        self.setParent(parent)
        self.setChildren(children)

    def setParent(self, newParent=Transform3Master.Master):
        newParent.addChild(self)

    def globalPosRotScale3(self):
        return self.localPosRotScale3.relative(self.parent.globalPosRotScale3())

    def __str__(self):
        return "Transform3 of local "+str(self.localPosRotScale3) + " with "+str(len(self.children)) + " children"
