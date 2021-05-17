from track import *
from mesh import *
import numpy as np

autoLinspace = lambda start, stop, pointsEvery1: np.linspace(
    start, stop, int(pointsEvery1 * np.abs(stop - start)))


class TrackMesh(Mesh):
    def __init__(self, track, pointsEvery1=2):

        ts = autoLinspace(track.tStart, track.tEnd, pointsEvery1)
        numPoints = len(ts)
        xs = [track.xt(t) for t in ts]
        ys = [track.yt(t) for t in ts]
        zs = [track.zt(t) for t in ts]

        self.points = [Vector3(xs[i], ys[i], zs[i]) for i in range(numPoints)]
        self.segs = [[i, i + 1] for i in range(numPoints - 1)]
        self.tris = []
