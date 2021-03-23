from vector import *


class Vector2(Vector):

    def __init__(self, x=0, y=0):
        self.c = [x, y]

    def __str__(self):
        return "Vector2(x = " + str(self.x)+", y = "+str(self.y)+")"


Vector2.zero = Vector2(0, 0)
Vector2.one = Vector2(1, 1)
Vector2.right = Vector2(1, 0)
Vector2.forward = Vector2(0, 1)
Vector2.left = Vector2(-1, 0)
Vector2.back = Vector2(0, -1)
