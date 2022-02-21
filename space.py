# A script containing several useful classes for 3D.

import numpy as np

from utilities import *

# A Vector is representend as a list of float coordinates.


class Vector(object):

    def __init__(self, c=[0, 0]):
        self.c = c

    @property
    def x(self): return self.c[0]

    @x.setter
    def x(self, value): self.c[0] = value

    @property
    def y(self): return self.c[1]

    @y.setter
    def y(self, value): self.c[1] = value

    @property
    def z(self): return self.c[2]

    @z.setter
    def z(self, value): self.c[2] = value

    def __eq__(a, b):
        return a.c == b.c

    def __ne__(a, b):
        return not a == b

    @property
    def sqrModule(a):
        return sum([k**2 for k in a.c])

    @property
    def module(a):
        return np.sqrt(a.sqrModule)

    def distance(a, b):
        return (a-b).module

    @property
    def normalized(a):
        m = a.module
        return a if m == 0 else a / m

    @property
    def toVector2(a):
        return Vector2(a.x, a.y)

    @property
    def toVector3(a):
        return Vector3(a.x, a.y, 0)

    def toTuple(self):
        return tuple(self.c)

    def __str__(self):
        return "Vector of coordinates(" + str([str(k) for k in self.c]) + ")"


# A Vector2 is a 2-dimensional Vector.
class Vector2(Vector):

    def __init__(self, x=0, y=0):
        if isinstance(x, list) or isinstance(x, tuple):
            self.c = x
        else:
            self.c = [x, y]

    def __add__(a, b): return Vector2(a.x + b.x, a.y + b.y)
    def __neg__(a): return Vector2(-a.x, -a.y)
    def __sub__(a, b): return a + -b

    def __mul__(a, b):
        if isinstance(b, Vector2):
            return Vector2(a.x * b.x, a.y * b.y)
        elif isinstance(b, int) or isinstance(b, float):
            return Vector2(a.x * b, a.y * b)

    def __truediv__(a, b):
        if isinstance(b, Vector2):
            return Vector2(a.x / b.x, a.y / b.y)
        elif isinstance(b, int) or isinstance(b, float):
            return a * (1 / b)

    def __str__(self):
        return "Vector2(x = " + str(self.x) + ", y = " + str(self.y) + ")"


Vector2.zero = Vector2(0, 0)
Vector2.one = Vector2(1, 1)
Vector2.right = Vector2(1, 0)
Vector2.forward = Vector2(0, 1)
Vector2.left = Vector2(-1, 0)
Vector2.back = Vector2(0, -1)

# A Vector3 is a 3-dimensional Vector.


class Vector3(Vector):

    def __init__(self, x=0, y=0, z=0):
        if isinstance(x, list) or isinstance(x, tuple):
            self.c = x
        else:
            self.c = [x, y, z]

    def __add__(a, b): return Vector3(a.x + b.x, a.y + b.y, a.z + b.z)
    def __neg__(a): return Vector3(-a.x, -a.y, -a.z)
    def __sub__(a, b): return a + -b

    def __mul__(a, b):
        if isinstance(b, Vector3):
            return Vector3(a.x * b.x, a.y * b.y, a.z * b.z)
        elif isinstance(b, int) or isinstance(b, float):
            return Vector3(a.x * b, a.y * b, a.z * b)

    def __truediv__(a, b):
        if isinstance(b, Vector3):
            return Vector3(a.x / b.x, a.y / b.y, a.z / b.z)
        elif isinstance(b, int) or isinstance(b, float):
            return a * (1 / b)

    # Dot product.
    def dot(a, b):
        return a.x * b.x + a.y * b.y + a.z * b.z

    # Cross product.
    def cross(a, b):
        return Vector3(a.y * b.z - a.z * b.y,
                       a.z * b.x - a.x * b.z,
                       a.x * b.y - a.y * b.x)

    def sinAngleBetween(a, b):
        return Vector3.cross(a.normalized,
                             b.normalized).module

    @property
    def toQuaternion(a):
        return Quaternion(0, a)

    def __str__(self):
        return "Vector3(x = " + str(self.x) + ", y = " + str(self.y) + ", z = " + str(self.z) + ")"


Vector3.zero = Vector3(0, 0, 0)
Vector3.one = Vector3(1, 1, 1)
Vector3.right = Vector3(1, 0, 0)
Vector3.forward = Vector3(0, 1, 0)
Vector3.up = Vector3(0, 0, 1)
Vector3.left = Vector3(-1, 0, 0)
Vector3.back = Vector3(0, -1, 0)
Vector3.down = Vector3(0, 0, -1)

# A Quaternion is a 4D number system, extending the complex number system.
# It is an efficient and compact way to compute 3D rotations.


class Quaternion:

    def __init__(self, w=1, v=Vector3()):
        self.w = w  # scalar part
        self.v = v  # vector part

    # Converts euler angles represented in a Vector3 to a rotation represented in a quaternion
    def eulerToQuaternion(euler):
        return Quaternion.angleAxis(euler.z, Vector3.up) * Quaternion.angleAxis(euler.y, Vector3.forward) * Quaternion.angleAxis(euler.x, Vector3.right)

    @ property
    def conjugate(a):
        return Quaternion(a.w, -a.v)

    @ property
    def sqrModule(a):
        return a.w**2 + a.v.sqrModule

    @ property
    def module(a):
        return np.sqrt(a.sqrModule)

    @ property
    def normalized(a):
        return a / a.module

    def __mul__(a, b):
        if isinstance(b, Quaternion):
            return Quaternion(a.w * b.w - Vector3.dot(a.v, b.v), b.v * a.w + a.v * b.w + Vector3.cross(a.v, b.v))
        elif isinstance(b, complex):
            return Quaternion(a.w * b, a.v * b)

    def __truediv__(a, b: complex):
        return Quaternion(a.w / b, a.v / b)

    # Computes b.a.b^-1.
    def compose(a, b):
        return b * (a * b.conjugate)

    # Computes the position of a Vector3 point rotated by a Quaternion rotation.
    def rotatedPoint(rotation, point):
        return Quaternion.compose(point.toQuaternion, rotation).v

    # Provides a Quaternion representing a rotation of a float angle around a Vector3 axis. (Theorem of equ)
    def angleAxis(angle, axis):
        semiAngle = angle * .5
        return Quaternion(np.cos(semiAngle), axis.normalized * np.sin(semiAngle))

    # Composes rotation, returning a composition of rotations.
    def rotated(self, b):
        return b * self

    # Represents the right direction of the object. Can be set to modify the rotation.
    @ property
    def localRight(self): return self.rotatedPoint(Vector3.right)

    @ localRight.setter
    def localRight(self, value):
        self.copy(Quaternion.fromToRotation(Vector3.right, value))

    # Represents the forward direction of the object. Can be set to modify the rotation.
    @ property
    def localForward(self): return self.rotatedPoint(Vector3.forward)

    @ localForward.setter
    def localForward(self, value):
        self.copy(Quaternion.fromToRotation(Vector3.forward, value))

    # Represents the up direction of the object. Can be set to modify the rotation.
    @ property
    def localUp(self): return self.rotatedPoint(Vector3.up)

    @ localUp.setter
    def localUp(self, value):
        self.copy(Quaternion.fromToRotation(Vector3.up, value))

    # Computes a Quaternion representing a rotation going from directions startVector to endVector.
    def fromToRotation(startVector, endVector):
        if startVector == endVector:
            return Quaternion.zero
        return Quaternion(np.sqrt(startVector.sqrModule * endVector.sqrModule) + startVector.dot(endVector), startVector.cross(endVector)).normalized

    # Computes a Quaternion rotation with specified forward and up directions, using rotation matrices.
    def facing(forward, up):

        up = up.normalized

        v0 = up.normalized
        v1 = (Vector3.cross(forward, v0)).normalized
        v2 = Vector3.cross(v0, v1)
        m00 = v1.x
        m01 = v1.y
        m02 = v1.z
        m10 = v2.x
        m11 = v2.y
        m12 = v2.z
        m20 = v0.x
        m21 = v0.y
        m22 = v0.z

        num8 = (m00 + m11) + m22
        q = Quaternion(0, Vector3(0, 0, 0))
        if num8 > 0:
            num = np.sqrt(num8 + 1)
            q.w = num * .5
            num = .5 / num
            q.v.x = (m12 - m21) * num
            q.v.y = (m20 - m02) * num
            q.v.z = (m01 - m10) * num
            return q

        if ((m00 >= m11) and (m00 >= m22)):
            num7 = np.sqrt(((1 + m00) - m11) - m22)
            num4 = .5 / num7
            q.v.x = .5 * num7
            q.v.y = (m01 + m10) * num4
            q.v.z = (m02 + m20) * num4
            q.w = (m12 - m21) * num4
            return q

        if (m11 > m22):
            num6 = np.sqrt(((1 + m11) - m00) - m22)
            num3 = .5 / num6
            q.v.x = (m10 + m01) * num3
            q.v.y = .5 * num6
            q.v.z = (m21 + m12) * num3
            q.w = (m20 - m02) * num3
            return q

        num5 = np.sqrt(((1 + m22) - m00) - m11)
        num2 = .5 / num5
        q.v.x = (m20 + m02) * num2
        q.v.y = (m21 + m12) * num2
        q.v.z = .5 * num5
        q.w = (m01 - m10) * num2
        return q

    def face(self, forward, up=Vector3(0, 0, 1)):
        self.copy(Quaternion.facing(forward, up))

    def copy(self, rot):
        self.w = rot.w
        self.v = rot.v

    def __set__(self, instance, value):
        self.w = value.w
        self.v = value.v

    def __str__(self):
        return "Quaternion(w = " + str(self.w) + ", x = " + str(self.v.x) + ", y = " + str(self.v.y) + ", z = " + str(self.v.z) + ")"


Quaternion.zero = Quaternion(1, Vector3())
