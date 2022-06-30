# A roller coaster track layout created by integrating a set of differential equations.

from matplotlib.pyplot import semilogx
from track import *
from physics import *
import numpy as np
import utilities

import scipy.integrate as scint


class TrackIntegrator(Track):

    def __init__(self, sampleDist=1):
        self.sampleDist = sampleDist
        self.sample()

    def sample(self):

        ds = self.sampleDist

        # Constant G function.

        def G(s): return 3

        # # Parabola G function.

        # def G(s): return (-1/1225)*s**2 + (101/1225)*s + ( 101/1225)

        # # Airtime Hill

        # def G(x): return - 13/649687500*x**6 + 3137/866250000*x**5 - 129641/519750000 * \
        #     x**4 + 281777/34650000*x**3 - 2567651/20790000*x**2 + 89147/138600*x + 1

        vi = 25
        sqrvi_divbyg = vi**2/g

        self.ClothoidIntegration(-34, 0)
        # self.ExternalIntegration(G, sqrvi_divbyg, -20,
        #                          0, 90)

        self.lt = len(self.points)
        self.maxDist = self.lt*self.sampleDist

        # Adds lateral displacement.
        for i in range(self.lt):
            self.points[i].y = 2*np.tanh((0+i-self.lt*.5)*10/self.lt)

    # Applies Euler's integration method.
    def CustomIntegration(self, G, sqrvi_divbyg, initialx, initialHeight, trackLength):
        angle = 0

        s = 0
        gIntegral = 0
        self.points = []

        ds = self.sampleDist

        pos = Vector3(initialx, 0, initialHeight)
        self.start = pos
        self.points.append(pos)

        for _ in range(5):
            pos += Vector3(ds, 0, 0)
            self.points.append(pos)

        while(s <= trackLength):
            cos = np.cos(angle)
            sin = np.sin(angle)

            angle += ((G(s)-cos)/(sqrvi_divbyg - 2 *
                                  (pos.z + fric*gIntegral)))*ds

            dx = cos * ds
            dh = sin * ds
            dpos = Vector3(dx, 0, dh)
            pos += dpos
            s += ds
            gIntegral += ds*np.abs(G(s))

            self.points.append(pos)

        self.end = pos
        self.lt = len(self.points)
        self.maxDist = self.lt*self.sampleDist

    # Uses Python's functionality to integrate numerically a set of differential equations.
    def ExternalIntegration(self, G, sqrvi_divbyg, initialx, initialHeight, trackLength):

        ss = np.linspace(0, trackLength, int(trackLength/(self.sampleDist)))

        # Function used to solve a set of differential equations:
        # When l = [angle, x, h]
        # d angle/ds = f(l,s) [0]
        # dx/ds = f(l,s) [1]
        # dh/ds = f(l,s) [2]
        def f(l, s):
            angle = l[0]
            x = l[1]
            h = l[2]

            cos = np.cos(angle)
            sin = np.sin(angle)

            return [
                (G(s)-cos)/(sqrvi_divbyg-2*(h + 0*fric*3*s)),
                cos,
                sin]

        sol = scint.odeint(f, [0, 0, initialHeight], ss)

        self.points = [Vector3(initialx+k[1], 0, k[2]) for k in sol]

        self.start = self.points[0]
        self.end = self.points[-1]

    def ClothoidIntegration(self, initialx, initialHeight, A=.0012):

        trackLength = np.sqrt(np.pi/A)

        ss = np.linspace(0, trackLength, int(trackLength/(self.sampleDist)))

        # Function used to solve a set of differential equations:
        # When l = [angle, x, h]
        # d angle/ds = f(l,s) [0]
        # dx/ds = f(l,s) [1]
        # dh/ds = f(l,s) [2]
        def f(l, s):
            angle = l[0]
            x = l[1]
            h = l[2]

            cos = np.cos(angle)
            sin = np.sin(angle)

            return [
                2*A*s,
                cos,
                sin]

        sol = scint.odeint(f, [0, 0, initialHeight], ss)

        ds = self.sampleDist
        self.points = []
        pos = Vector3(initialx, 0, initialHeight)
        for _ in range(15):
            pos += Vector3(ds, 0, 0)
            self.points.append(pos)

        self.points.extend([Vector3(pos.x+k[1], 0, k[2]) for k in sol])

        # Mirror second part of loop:
        middle = self.points[-1]

        mirror = self.points[::-1]
        mirror.pop(0)

        for k in mirror:
            self.points.append(Vector3(2*middle.x-k.x, k.y, k.z))

        self.start = self.points[0]
        self.end = self.points[-1]

    # Linear interpolation between two points.

    def Lerp2Points(self, point1, point2, t):
        return point1+(point2-point1)*t

    def AffineCurve(self, dist):
        if dist <= 0:
            return self.start
        if dist >= self.maxDist-self.sampleDist:
            return self.end

        d = 0
        i = 0
        while d <= dist-1:
            d += self.sampleDist
            i += 1
        return self.Lerp2Points(self.points[i], self.points[i+1], dist-d)


TrackIntegrator.TearLoop = TrackIntegrator()
