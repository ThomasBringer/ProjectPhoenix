# A Mesh is a way to represent 3D geometry.
# Meshes are made of:
# - a list of Vector3, which represents vertex positions;
# - a list of lists of 2 integers, which represents the indices of the vertices for the start and the end of a segment;
# - a list of lists of 3 integers, which represents the indices of the corners of a triangle.

from transform3 import *
from unit import *


class Mesh():
    def __init__(self, points=[], segs=[], tris=[]):  # , entity, transform):
        self.points = points
        self.segs = segs
        self.tris = tris

    def __str__(self):
        return "Mesh made of " + str(len(self.points)) + " points, " + str(len(self.segs)) + " segments and " + str(len(self.tris)) + " triangles"


# A cube Mesh.
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

# A pyramid Mesh.
Mesh.Pyramid = Mesh([Vector3(1, -1, 0) * .5, Vector3(1, 1, 0) * .5,
                     Vector3(-1, -1, 0) * .5, Vector3(-1, 1, 0) * .5,
                     Vector3(0, 0, 1)],
                    [[0, 1], [0, 2], [1, 3], [2, 3],
                     [0, 4], [1, 4], [2, 4], [3, 4]],
                    [[0, 1, 3], [0, 2, 3], [0, 1, 4], [0, 2, 4], [1, 3, 4], [2, 3, 4]])

# A roller coaster cart Mesh.
Mesh.Cart = Mesh([Vector3(0.587189, -1.5, 0.270633), Vector3(-0.587189, -1.5, 0.270633),
                  Vector3(0.587189, 1.5, 0.270633), Vector3(-0.587189,
                                                            1.5, 0.270633),

                  Vector3(0.704225, -1.5,
                          0.770633), Vector3(-0.704225, -1.5, 0.770633),
                  Vector3(0.704225, -.9,
                          0.770633), Vector3(-0.704225, -.9, 0.770633),
                  Vector3(0.704225, -.3,
                          0.770633), Vector3(-0.704225, -.3, 0.770633),
                  Vector3(0.704225, .3,
                          0.770633), Vector3(-0.704225, .3, 0.770633),
                  Vector3(0.704225, .9,
                          0.770633), Vector3(-0.704225, .9, 0.770633),
                  Vector3(0.704225, 1.5, 0.770633), Vector3(-0.704225,
                                                            1.5, 0.770633),

                  Vector3(0.704225, 0.9,
                          1.27063), Vector3(-0.704225, 0.9, 1.27063),

                  Vector3(0.56338, -1.41,
                          1.77063), Vector3(-0.56338, -1.41, 1.77063),
                  Vector3(0.56338, -0.99,
                          1.77063), Vector3(-0.56338, -0.99, 1.77063),
                  Vector3(0.56338, -0.21,
                          1.77063), Vector3(-0.56338, -0.21, 1.77063),
                  Vector3(0.56338, .21, 1.77063), Vector3(-0.56338, .21, 1.77063)],

                 [[0, 1], [0, 2], [0, 4],
                  [1, 3], [1, 5],
                  [2, 3], [2, 14],
                  [3, 15],

                  [4, 18],
                  [5, 19],
                  [6, 7], [6, 8], [6, 20],
                  [7, 9], [7, 21],
                  [8, 9], [8, 22],
                  [9, 23],
                  [10, 11], [10, 12], [10, 24],
                  [11, 13], [11, 25],
                  [12, 13], [12, 16],
                  [13, 17],
                  [14, 16],
                  [15, 17],

                  [16, 17],

                  [18, 19], [18, 20], [19, 21], [20, 21],
                  [22, 23], [22, 24], [23, 25], [24, 25]],

                 [[0, 1, 2], [1, 2, 3],
                  [0, 2, 4], [2, 4, 14],
                  [1, 3, 5], [3, 5, 15],
                  [0, 1, 4], [1, 4, 5],
                  [2, 3, 14], [3, 14, 15],

                  [4, 5, 18], [5, 18, 19],
                  [6, 7, 20], [7, 20, 21],
                  [4, 6, 18], [6, 18, 20],
                  [5, 7, 19], [7, 19, 21],
                  [18, 19, 20], [19, 20, 21],

                  [8, 9, 22], [9, 22, 23],
                  [10, 11, 24], [11, 24, 25],
                  [8, 10, 22], [10, 22, 24],
                  [9, 11, 23], [11, 23, 25],
                  [22, 23, 24], [23, 24, 25],

                  [12, 14, 16], [13, 15, 17],
                  [12, 13, 16], [13, 16, 17],
                  [14, 15, 16], [15, 16, 17]])

# A flat plane Mesh.
Mesh.Ground = Mesh([Vector3(-2, -2, 0), Vector3(-1, -2, 0), Vector3(0, -2, 0), Vector3(1, -2, 0), Vector3(2, -2, 0),
                    Vector3(-2, -1, 0), Vector3(2, -1, 0),
                    Vector3(-2, 0, 0), Vector3(2, 0, 0),
                    Vector3(-2, 1, 0), Vector3(2, 1, 0),
                    Vector3(-2, 2, 0), Vector3(-1, 2, 0), Vector3(0, 2, 0), Vector3(1, 2, 0), Vector3(2, 2, 0)],
                   [[0, 11], [1, 12], [2, 13], [3, 14], [4, 15],
                    [0, 4], [5, 6], [7, 8], [9, 10], [11, 15]],
                   [[0, 4, 11], [4, 11, 15]])
