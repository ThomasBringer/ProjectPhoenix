class Matrix2x2:

    # M = (x y
    #      z t)

    # x = 0
    # y = 0
    # z = 0
    # t = 0

    def __init__(self, x=0, y=0, z=0, t=0):
        self.x = x
        self.y = y
        self.z = z
        self.t = t

    def __add__(a, b): return Matrix2x2(a.x+b.x, a.y+b.y, a.z+b.z, a.t+b.t)
    def __neg__(a): return Matrix2x2(-a.x, -a.y, -a.z, -a.t)
    def __sub__(a, b): return a+-b

    def __mul__(a, b):
        return Matrix2x2(a.x*b.x+a.y*b.z,    a.x*b.y+a.y*b.t,    a.z*b.x+a.t*b.z,    a.z*b.y+a.t*b.t)

    #def __mul__(a,b:complex): return Matrix2x2(a.x*b,a.y*b,a.z*b,a.t*b)

    def __str__(self):
        return "Matrix2x2("+str(self.x)+", "+str(self.y)+", "+str(self.z)+", "+str(self.t)+")"


Matrix2x2.U = Matrix2x2(1, 0, 0, 1)
Matrix2x2.I = Matrix2x2(1j, 0, 0, -1j)
Matrix2x2.J = Matrix2x2(0, 1, -1, 0)
Matrix2x2.K = Matrix2x2(0, 1j, 1j, 0)

# print(Matrix2x2.J*Matrix2x2.K)
