from track import *
from mesh import *
import numpy as np


def autoLinspace(start, stop, pointsEvery1):
    return np.linspace(start, stop, int(pointsEvery1 * np.abs(stop - start)))


class TrackMesh(Mesh):
    def __init__(self, track):

        #ts = autoLinspace(track.tStart, track.tEnd, pointsEvery1)

        self.points = [track.Curve(t) for t in track.ts]
        self.segs = [[i, i + 1] for i in range(track.lt - 1)]
        self.tris = []
