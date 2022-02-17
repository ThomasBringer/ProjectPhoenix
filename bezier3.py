# from utilities import *
# from space import *


# class Bezier3:

#     def __init__(self, points, handles, sampleDist=1):  # ,tilts
#         self.points = points
#         self.handles = handles
#         # self.tilts=tilts
#         self.sampleDist = sampleDist
#         self.ts = self.sample(sampleDist)

#         self.lt = len(self.ts)
#         self.maxDist = (self.lt-1)*sampleDist
#         self.step = 1/(self.lt*self.sampleDist)
#         sampledPoints = [self.Curve(t) for t in self.ts]
#         segLengths = [Vector.distance(
#             sampledPoints[i], sampledPoints[i+1]) for i in range(self.lt-1)]
#         # print("hey", segLengths)

#     def sample(self, sampleDist, eps=.0001, tryT=.01):
#         ts = [0]
#         t = 0
#         while True:
#             i = 1
#             t += tryT
#             if 1 < t:
#                 return ts

#             diff = Vector.distance(self.Curve(
#                 ts[-1]), self.Curve(t)) - sampleDist
#             while eps < np.abs(diff):
#                 t -= np.sign(diff)*tryT*(.5**i)
#                 if 1 < t:
#                     return ts
#                 i += 1
#                 diff = Vector.distance(self.Curve(
#                     ts[-1]), self.Curve(t)) - sampleDist
#             ts.append(t)

#     @property
#     def start(self): return self.points[0]

#     @property
#     def end(self): return self.points[-1]

#     # Returns a simple 2-point Bezier curve evaluated at t between 0 and 1.
#     def Curve2Points(point1, point2, handle1, handle2, t=0):
#         return point1*((1-t)**3)+handle1*(3*t*((1-t)**2))+handle2*(3*(t**2)*(1-t)) + point2*(t**3)

#     # Returns a full Bezier curve with several points and handles, evaluated at t between 0 and 1.
#     def Curve(self, t):
#         if t <= 0:
#             return self.start
#         if t >= 1:
#             return self.end

#         newT = (len(self.points)-1)*t
#         i = int(newT)
#         # print(newT, i)
#         relativeT = newT-i
#         return Bezier3.Curve2Points(self.points[i], self.points[i+1], self.handles[2*i], self.handles[2*i+1], relativeT)

#     def Lerp2Points(self, point1, point2, t):
#         return point1+(point2-point1)*t

#     def FakeCurve(self, dist):
#         if dist <= 0:
#             return self.start
#         if dist >= self.maxDist:
#             return self.end

#         d = 0
#         i = 0
#         while d <= dist-1:
#             d += self.sampleDist
#             i += 1

#         return self.Lerp2Points(self.Curve(self.ts[i]), self.Curve(self.ts[i+1]), dist-d)

#     def DistToT(self, dist):
#         return self.step*dist
#         #t = dist*self.invTotalLength
#         # diff = (self.TToDist(t)-dist)

#         # print("t:", t, "diff:", diff)

#         # while eps < np.abs(diff):  # or t < 0 or 1 < t:
#         #     t += diff*self.invTotalLength
#         #     diff = dist - self.TToDist(t)
#         #     print("t:", t, "diff:", diff)

#         # t = clamp(t)
#         # print("FOUND!", t)
#         # return t

#     def TToDist(self, t):
#         # print(self.segLengths)
#         ti = 0
#         i = 0
#         dist = 0
#         while ti <= t:
#             dist += self.segLengths[i]
#             i += 1
#             ti += self.step
#             # print(ti, t)
#         dist += ((self.step-(ti-t))/self.step)*self.segLengths[i]
#         return dist


# Bezier3.DropRoundLoop = Bezier3(
#     [Vector3(-45, -5, 45),
#      Vector3(0, -5, 0),
#      Vector3(15, -2.5, 15),
#      Vector3(0, 0, 30),
#      Vector3(-15, 2.5, 15),
#      Vector3(0, 5, 0),
#      Vector3(25, 5, 7.5)],

#     [Vector3(-35, -5, 30),
#      Vector3(-15, -5, 0),
#      Vector3(7.5, -5, 0),
#      Vector3(15, -3.70702, 7.5251),
#      Vector3(15, -1.30924, 22.3742),
#      Vector3(7.5, 0, 30),
#      Vector3(-7.5, 0, 30),
#      Vector3(-15, 1.4082, 22.3802),
#      Vector3(-15, 3.60757, 7.51317),
#      Vector3(-7.5, 5, 0),
#      Vector3(7.5, 5, 0),
#      Vector3(17.5, 5, 2.5)])

# Bezier3.DropOvalLoop = Bezier3(
#     [Vector3(-45, -5, 45),
#      Vector3(-5, -5, 0),
#      Vector3(10, -1.875, 20),
#      Vector3(0, 0, 30),
#      Vector3(-10, 1.875, 20),
#      Vector3(5, 5, 0),
#      Vector3(25, 5, 7.5)],

#     [Vector3(-35, -5, 30),
#      Vector3(-20, -5, 0),
#      Vector3(2.5, -5, 0),
#      Vector3(10, -2.78026, 11.2545),
#      Vector3(10, -1.29818, 25.5725),
#      Vector3(5.625, 0, 30),
#      Vector3(-5.625, 0, 30),
#      Vector3(-10, 1.34645, 25.5704),
#      Vector3(-10, 2.70567, 11.2455),
#      Vector3(-2.5, 5, 0),
#      Vector3(12.5, 5, 0),
#      Vector3(17.5, 5, 2.5)])

# Bezier3.RoundLoop = Bezier3(
#     [Vector3(-45, -5, 0),
#      Vector3(0, -5, 0),
#      Vector3(15, -2.5, 15),
#      Vector3(0, 0, 30),
#      Vector3(-15, 2.5, 15),
#      Vector3(0, 5, 0),
#      Vector3(25, 5, 7.5)],

#     [Vector3(-35, -5, 0),
#      Vector3(-15, -5, 0),
#      Vector3(7.5, -5, 0),
#      Vector3(15, -3.70702, 7.5251),
#      Vector3(15, -1.30924, 22.3742),
#      Vector3(7.5, 0, 30),
#      Vector3(-7.5, 0, 30),
#      Vector3(-15, 1.4082, 22.3802),
#      Vector3(-15, 3.60757, 7.51317),
#      Vector3(-7.5, 5, 0),
#      Vector3(7.5, 5, 0),
#      Vector3(17.5, 5, 2.5)])

# Bezier3.OvalLoop = Bezier3(
#     [Vector3(-45, -5, 0),
#      Vector3(-5, -5, 0),
#      Vector3(10, -1.875, 20),
#      Vector3(0, 0, 30),
#      Vector3(-10, 1.875, 20),
#      Vector3(5, 5, 0),
#      Vector3(25, 5, 7.5)],

#     [Vector3(-35, -5, 0),
#      Vector3(-20, -5, 0),
#      Vector3(2.5, -5, 0),
#      Vector3(10, -2.78026, 11.2545),
#      Vector3(10, -1.29818, 25.5725),
#      Vector3(5.625, 0, 30),
#      Vector3(-5.625, 0, 30),
#      Vector3(-10, 1.34645, 25.5704),
#      Vector3(-10, 2.70567, 11.2455),
#      Vector3(-2.5, 5, 0),
#      Vector3(12.5, 5, 0),
#      Vector3(17.5, 5, 2.5)])
