import numpy as np
from unit import *
from vector3 import *

zero = lambda t: 0
const = lambda t: t


class Track(Unit):
    def __init__(self, xt=zero, yt=const, zt=zero, tStart=0, tEnd=1):
        self.xt = xt
        self.yt = yt
        self.zt = zt
        self.tStart = tStart
        self.tEnd = tEnd

    post = lambda self, t: Vector3(self.xt(t), self.yt(t), self.zt(t))

    # def post(self, t):
    #     return Vector3(self.xt[t], self.yt[t], self.zt[t])

    @property
    def start(self):
        return self.post(self.tStart)

    @property
    def end(self):
        return self.post(self.tEnd)


f = lambda t: 2 * t * np.cos(t * .25)
g = lambda t: 8 * np.sin(t * .25)
# g = lambda t: -(t * .5) * np.cos(t * .5)

Track.T01 = Track(g, const, f, -np.pi * 4, np.pi * 4)
# Track.T02 = Track(zero, const, g, -np.pi * .5, np.pi * 3)

# Track.T01 = Track([Vector3(0, -3, 3), Vector3(0, -2, 1.5), Vector3(0, -1, 1),
#                    Vector3(0, 0, 0), Vector3(0, 1, -1.5), Vector3(0, 2, -2)])
