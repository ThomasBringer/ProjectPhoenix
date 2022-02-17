from track import *
from physics import *
import numpy as np
import utilities


class TrackIntegrator(Track):

    def __init__(self, sampleDist=1):
        self.sampleDist = sampleDist
        self.sample()

    def sample(self):
        ds = self.sampleDist

        # # airtime
        # a = 1/600
        # b = -17/200
        # c = 13/12

        a = -1/1225
        b = 101/1225
        c = 45/49

        def G(s): return 3  # a*s**2 + b*s + c
        # 2.5-.001*(s-50)**2
        # 1.5+.001*(s-50)**2
        # 2.5+.0002*(s-50)**2

        vi = 25
        sqrvi_divbyg = vi**2/g

        angle = 0

        s = 0
        self.points = []

        pos = Vector3(-33, 0, 0)
        self.start = pos
        self.points.append(pos)

        for _ in range(5):
            pos += Vector3(ds, 0, 0)
            self.points.append(pos)

        while(s <= 100):
            cos = np.cos(angle)
            sin = np.sin(angle)
            angle += ((G(s)-cos)/(sqrvi_divbyg-2*(pos.z)))*ds

            dx = cos * ds
            dh = sin * ds
            dpos = Vector3(dx, 0, dh)
            pos += dpos
            s += ds

            self.points.append(pos)

        # print("diff angle",angle)

        # dpos = Vector3(-ds, 0, 0)
        # pos += dpos
        # s += ds

        # self.points.append(pos)

        # middlex = pos.x

        # morepoints = list(reversed(copy(self.points)))
        # for k in morepoints:
        #     k.x = 2*middlex - k.x
        # self.points.extend(morepoints)

        # for _ in range(10):
        #     pos += Vector3(ds, 0, 0)
        #     self.points.append(pos)

        self.end = pos
        self.lt = len(self.points)
        self.maxDist = self.lt*self.sampleDist

        ts = np.linspace(-5, 5, self.lt-5)
        for i in range(5):
            self.points[i].y = 2*np.tanh(ts[5])
        for i in range(self.lt-5):
            self.points[i+5].y = 2*np.tanh(ts[i])

    def Lerp2Points(self, point1, point2, t):
        return point1+(point2-point1)*t

    def FakeCurve(self, dist):
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


TrackIntegrator.ConstantG = TrackIntegrator()
