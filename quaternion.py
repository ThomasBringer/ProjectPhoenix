from vector3 import *
# from matrix2x2 import *


class Quaternion:

    # q = w + ix + jy + kz

    def __init__(self, w=1, x=0, y=0, z=0):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def fromVectorial(w, vector3):
        return Quaternion(w, vector3.x, vector3.y, vector3.z)

    def toOnlyVectorial(a):
        return Vector3(a.x, a.y, a.z)

    def toVectorial(a):
        return a.w, a.toOnlyVectorial()

    def eulerToQuaternion(euler):
        # print(euler)
        # print(euler.x, euler.y, euler.z)
        return Quaternion.angleAxis(euler.z, Vector3.up) * Quaternion.angleAxis(euler.y, Vector3.forward) * Quaternion.angleAxis(euler.x, Vector3.right)

    @property
    def conjugate(a):
        return Quaternion(a.w, -a.x, -a.y, -a.z)

    @property
    def sqrModule(a):
        return a.w**2 + a.x**2 + a.y**2 + a.z**2

    @property
    def module(a):
        return np.sqrt(a.sqrModule)

    @property
    def normalized(a):
        return a / a.module

    # def inverse(a):
    #     return a.conjugate/a.sqrModule

    def __mul__(a, b):
        if isinstance(b, Quaternion):
            wa, va = a.toVectorial()
            wb, vb = b.toVectorial()
            return Quaternion.fromVectorial(wa * wb - Vector3.dotProduct(va, vb), vb * wa + va * wb + Vector3.crossProduct(va, vb))
        elif isinstance(b, complex):
            return Quaternion(a.w * b, a.x * b, a.y * b, a.z * b)

    def __truediv__(a, b: complex):
        return Quaternion(a.w / b, a.x / b, a.y / b, a.z / b)

    def compose(a, b):  # = bab-1
        return b * (a * b.conjugate)

    def rotatedPoint(rotation, point):
        return Quaternion.compose(Quaternion.fromVectorial(0, point), rotation).toOnlyVectorial()

    def angleAxis(angle, axis):
        semiAngle = angle * .5
        return Quaternion.fromVectorial(np.cos(semiAngle), axis.normalized * np.sin(semiAngle))

    def rotated(self, b):
        return b * self

    @property
    def localRight(self): return self.rotatedPoint(Vector3.right)

    @localRight.setter
    def localRight(self, value):
        self.copy(Quaternion.fromToRotation(Vector3.right, value))

    @property
    def localForward(self): return self.rotatedPoint(Vector3.forward)

    @localForward.setter
    def localForward(self, value):
        self.copy(Quaternion.fromToRotation(Vector3.forward, value))

    @property
    def localUp(self): return self.rotatedPoint(Vector3.up)

    @localUp.setter
    def localUp(self, value):
        self.copy(Quaternion.fromToRotation(Vector3.up, value))

    # def complexRep(a):
    #     return Matrix2x2.U*a.w + Matrix2x2.I*a.x + Matrix2x2.J*a.y + Matrix2x2.K*a.z

    def fromToRotation(startVector, endVector):
        return Quaternion.fromVectorial(np.sqrt(startVector.sqrModule * endVector.sqrModule) + startVector.dotProduct(endVector), startVector.crossProduct(endVector)).normalized

    def copy(self, rot):
        self.w = rot.w
        self.x = rot.x
        self.y = rot.y
        self.z = rot.z

    def __set__(self, instance, value):
        self.w = value.w
        self.x = value.x
        self.y = value.y
        self.z = value.z

    def __str__(self):
        return "Quaternion(w = " + str(self.w) + ", x = " + str(self.x) + ", y = " + str(self.y) + ", z = " + str(self.z) + ")"


Quaternion.zero = Quaternion(1, 0, 0, 0)
