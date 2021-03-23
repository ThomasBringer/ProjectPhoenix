from transform3 import *
from segment3 import *
from unit import *


Meshes = []


class Mesh(Unit):
    # points = []  # [Vector3.zero,Vector3.right,Vector3.right+Vector3.forward]
    # segments = []  # [[0,1],[1,2]]

    def __init__(self, points=[], segs=[], tris=[]):  # , entity, transform):
        self.points = points
        self.segs = segs
        self.tris = tris
        # Meshes.append(self)
        # self.entity = entity
        # self.transform = transform

    def globalPoints(self):
        # print(self.transform.globalPosRotScale3())

        parentPosRotScale3 = self.transform.globalPosRotScale3()
        #parentPos, parentRot, parentScale = parentPosRotScale3.position, parentPosRotScale3.rotation, parentPosRotScale3.scale
        return [PosRotScale3.relativePos(point, parentPosRotScale3) for point in self.points]

        # return [PosRotScale3(point).relativePos(parentPosRotScale3).position for point in self.points]

    # def globalSegs(self):
    #     globalPoints = self.globalPoints()
    #     return [Segment3(globalPoints[i[0]], globalPoints[i[1]]) for i in self.segs]

    def __str__(self):
        return "Mesh made of "+str(len(self.points))+" points, "+str(len(self.segs)) + " segments and "+str(len(self.tris)) + " triangles"


# Mesh.Cube = Mesh([Vector3(1, -1, -1)*.5, Vector3(1, 1, -1)*.5,
#                   Vector3(-1, -1, -1)*.5, Vector3(-1, 1, -1)*.5,
#                   Vector3(1, -1, 1)*.5, Vector3(1, 1, 1)*.5,
#                   Vector3(-1, -1, 1)*.5, Vector3(-1, 1, 1)*.5],
#                  [[0, 1], [0, 2], [1, 3], [2, 3],
#                   [0, 4], [1, 5], [2, 6], [3, 7],
#                   [4, 5], [4, 6], [5, 7], [6, 7]])

Mesh.Box = Mesh([Vector3(1, -1, -1)*.5, Vector3(1, 1, -1)*.5,
                 Vector3(-1, -1, -1)*.5, Vector3(-1, 1, -1)*.5,
                 Vector3(1, -1, 1)*.5, Vector3(1, 1, 1)*.5,
                 Vector3(-1, -1, 1)*.5, Vector3(-1, 1, 1)*.5],
                [[0, 1], [0, 2], [1, 3], [2, 3],
                 [0, 4], [1, 5], [2, 6], [3, 7],
                 [4, 5], [4, 6], [5, 7], [6, 7],
                 [0, 3], [0, 5], [0, 6], [3, 5], [3, 6], [5, 6]],
                [[0, 1, 3], [0, 2, 3],
                    [0, 1, 5], [0, 4, 5],
                    [0, 2, 6], [0, 4, 6],
                    [1, 3, 5], [3, 5, 7],
                    [2, 3, 6], [3, 6, 7],
                    [4, 5, 6], [5, 6, 7]])

Mesh.Pyramid = Mesh([Vector3(1, -1, 0)*.5, Vector3(1, 1, 0)*.5,
                     Vector3(-1, -1, 0)*.5, Vector3(-1, 1, 0)*.5,
                     Vector3(0, 0, 1)],
                    [[0, 1], [0, 2], [1, 3], [2, 3], [0, 3],
                     [0, 4], [1, 4], [2, 4], [3, 4]],
                    [[0, 1, 3], [0, 2, 3], [0, 1, 4], [0, 2, 4], [1, 3, 4], [2, 3, 4]])

# print([str(k)for k in Entit Mesh.Cube.globalPoints()])

# print([str(k)for k in Mesh.Cube.segments()])
