from transform3 import *
# from segment3 import *
from unit import *


class Mesh():
    def __init__(self, points=[], segs=[], tris=[]):  # , entity, transform):
        self.points = points
        self.segs = segs
        self.tris = tris

    def __str__(self):
        return "Mesh made of " + str(len(self.points)) + " points, " + str(len(self.segs)) + " segments and " + str(len(self.tris)) + " triangles"


# Mesh.Cube = Mesh([Vector3(1, -1, -1)*.5, Vector3(1, 1, -1)*.5,
#                   Vector3(-1, -1, -1)*.5, Vector3(-1, 1, -1)*.5,
#                   Vector3(1, -1, 1)*.5, Vector3(1, 1, 1)*.5,
#                   Vector3(-1, -1, 1)*.5, Vector3(-1, 1, 1)*.5],
#                  [[0, 1], [0, 2], [1, 3], [2, 3],
#                   [0, 4], [1, 5], [2, 6], [3, 7],
#                   [4, 5], [4, 6], [5, 7], [6, 7]])

Mesh.Cube = Mesh([Vector3(1, -1, -1) * .5, Vector3(1, 1, -1) * .5,
                  Vector3(-1, -1, -1) * .5, Vector3(-1, 1, -1) * .5,
                  Vector3(1, -1, 1) * .5, Vector3(1, 1, 1) * .5,
                  Vector3(-1, -1, 1) * .5, Vector3(-1, 1, 1) * .5],
                 [[0, 1], [0, 2], [1, 3], [2, 3],
                  [0, 4], [1, 5], [2, 6], [3, 7],
                  [4, 5], [4, 6], [5, 7], [6, 7]],
                 [[0, 1, 3], [0, 2, 3],
                  [0, 1, 5], [0, 4, 5],
                  [0, 2, 6], [0, 4, 6],
                  [1, 3, 5], [3, 5, 7],
                  [2, 3, 6], [3, 6, 7],
                  [4, 5, 6], [5, 6, 7]])

Mesh.Pyramid = Mesh([Vector3(1, -1, 0) * .5, Vector3(1, 1, 0) * .5,
                     Vector3(-1, -1, 0) * .5, Vector3(-1, 1, 0) * .5,
                     Vector3(0, 0, 1)],
                    [[0, 1], [0, 2], [1, 3], [2, 3],
                     #[0, 3],
                     [0, 4], [1, 4], [2, 4], [3, 4]],
                    [[0, 1, 3], [0, 2, 3], [0, 1, 4], [0, 2, 4], [1, 3, 4], [2, 3, 4]])

Mesh.Cart = Mesh([Vector3(1, -1.5, 0), Vector3(1, 1.5, 0),
                  Vector3(-1, -1.5, 0), Vector3(-1, 1.5, 0),
                  Vector3(1, -1.5, 1), Vector3(1, 1.5, 1),
                  Vector3(-1, -1.5, 1), Vector3(-1, 1.5, 1)],
                 [[0, 1], [0, 2], [1, 3], [2, 3],
                  [0, 4], [1, 5], [2, 6], [3, 7],
                  [4, 5], [4, 6], [5, 7], [6, 7]],
                 [[0, 1, 3], [0, 2, 3],
                  [0, 1, 5], [0, 4, 5],
                  [0, 2, 6], [0, 4, 6],
                  [1, 3, 5], [3, 5, 7],
                  [2, 3, 6], [3, 6, 7],
                  [4, 5, 6], [5, 6, 7]])

Mesh.Ground = Mesh([Vector3(-2, -2, 0), Vector3(-1, -2, 0), Vector3(0, -2, 0), Vector3(1, -2, 0), Vector3(2, -2, 0),
                    Vector3(-2, -1, 0), Vector3(2, -1, 0),
                    Vector3(-2, 0, 0), Vector3(2, 0, 0),
                    Vector3(-2, 1, 0), Vector3(2, 1, 0),
                    Vector3(-2, 2, 0), Vector3(-1, 2, 0), Vector3(0, 2, 0), Vector3(1, 2, 0), Vector3(2, 2, 0)],
                   [[0, 11], [1, 12], [2, 13], [3, 14], [4, 15],
                    [0, 4], [5, 6], [7, 8], [9, 10], [11, 15]],
                   [[0, 4, 11], [4, 11, 15]])
