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

        # # Constant G function.
        # def G(s): return 3  # a*s**2 + b*s + c

        # # Parabola G function.
        # G_max = 1.5
        # a = -(G_max)/(np.pi**2)
        # b = 2*(G_max)/np.pi
        # def G(angle): return a*angle**2 + b*angle+1.5

        # # Parabola G function.
        a = -1/1225
        b = 101/1225
        c = 45/49
        def G(s): return a*s**2 + b*s + c

        # Airtime Hill

        # def G(x): return - 13/649687500*x**6 + 3137/866250000*x**5 - 129641/519750000 * \
        #     x**4 + 281777/34650000*x**3 - 2567651/20790000*x**2 + 89147/138600*x + 1

        vi = 25
        sqrvi_divbyg = vi**2/g

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
                (G(s)-cos)/(sqrvi_divbyg-2*h),
                cos,
                sin]

        initialHeight = 0
        initialx = -35
        trackLength = 100

        ss = np.linspace(0, trackLength, int(trackLength/(self.sampleDist)))
        sol = scint.odeint(f, [0, 0, initialHeight], ss)

        self.points = [Vector3(initialx+k[1], 0, k[2]) for k in sol]

        self.start = self.points[0]
        self.end = self.points[-1]
        self.lt = len(self.points)
        self.maxDist = self.lt*self.sampleDist

        # Adds lateral displacement.
        for i in range(self.lt):
            self.points[i].y = 2*np.tanh((10+i-self.lt*.5)*10/self.lt)

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
