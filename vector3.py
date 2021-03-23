from vector import *


class Vector3(Vector):

    def __init__(self, x=0, y=0, z=0):
        self.c = [x, y, z]

    def dotProduct(a, b):
        return a.x*b.x+a.y*b.y+a.z*b.z

    def crossProduct(a, b):
        return Vector3(a.y*b.z-a.z*b.y, a.z*b.x-a.x*b.z, a.x*b.y-a.y*b.x)

    def __str__(self):
        return "Vector3(x = " + str(self.x)+", y = "+str(self.y)+", z = "+str(self.z)+")"


Vector3.zero = Vector3(0, 0, 0)
Vector3.one = Vector3(1, 1, 1)
Vector3.right = Vector3(1, 0, 0)
Vector3.forward = Vector3(0, 1, 0)
Vector3.up = Vector3(0, 0, 1)
Vector3.left = Vector3(-1, 0, 0)
Vector3.back = Vector3(0, -1, 0)
Vector3.down = Vector3(0, 0, -1)
