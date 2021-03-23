from vector3 import *
from matrix2x2 import *


class Quaternion:

    # q = w + ix + jy + kz

    # w = 1
    # x = 0
    # y = 0
    # z = 0

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
        return Quaternion.angleAxis(euler.z, Vector3.up)*Quaternion.angleAxis(euler.y, Vector3.forward)*Quaternion.angleAxis(euler.x, Vector3.right)

    def conjugate(a):
        return Quaternion(a.w, -a.x, -a.y, -a.z)

    # def sqrModule(a):
    #     return a.w**2+a.x**2+a.y**2+a.z**2

    # def module(a):
    #     return np.sqrt(a.sqrModule())

    # def inverse(a):
    #     return a.conjugate()/a.sqrModule()

    def __mul__(a, b):
        if isinstance(b, Quaternion):
            wa, va = a.toVectorial()
            wb, vb = b.toVectorial()
            #wa = float(wa)
            #wb = float(wb)
            return Quaternion.fromVectorial(wa*wb-Vector3.dotProduct(va, vb), vb*wa+va*wb+Vector3.crossProduct(va, vb))
        elif isinstance(b, complex):
            return Quaternion(a.w*b, a.x*b, a.y*b, a.z*b)

    def __truediv__(a, b: complex):
        return Quaternion(a.w/b, a.x/b, a.y/b, a.z/b)

    def compose(a, b):  # = bab-1
        return b*(a*Quaternion.conjugate(b))

    def rotatedPoint(rotation, point):
        return Quaternion.compose(Quaternion.fromVectorial(0, point), rotation).toOnlyVectorial()

    def angleAxis(angle, axis):
        semiAngle = angle*.5
        return Quaternion.fromVectorial(np.cos(semiAngle), axis.normalized()*np.sin(semiAngle))

    def rotated(self, b):
        return b*self

    # def angleAxisComposer(angle, axis):
    #     semiAngle=angle*.5
    #     return Quaternion.fromVectorial(np.cos(semiAngle),axis.normalized()*np.sin(semiAngle))

    # def angleAxis(point,angle,axis):
    #     return Quaternion.angleAxisComposer(angle,axis)).toOnlyVectorial()

    # def pointAngleAxis(point,angle,axis):
    #    return Quaternion.compose(Quaternion.fromVectorial(0,point),Quaternion.angleAxisComposer(angle,axis)).toOnlyVectorial()

    def complexRep(a):
        return Matrix2x2.U*a.w + Matrix2x2.I*a.x + Matrix2x2.J*a.y + Matrix2x2.K*a.z

    def __str__(self):
        return "Quaternion(w = "+str(self.w)+", x = " + str(self.x)+", y = "+str(self.y)+", z = "+str(self.z)+")"


#Quaternion.zero = Quaternion(1, 0, 0, 0)

someQuaternion = Quaternion(0.965472, -0.129223, -0.167752, -0.151738)

# q = Quaternion.pointAngleAxis(Vector3.one,-np.pi*.25,Vector3.up)

# p=Quaternion(0.965926,0,0,0.258819)
# v=Quaternion.fromVectorial(0,Vector3.one)

# print(Quaternion.compose(v,p))
