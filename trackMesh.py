# A Unit used to show a 3D roller coaster track layout as a 3D mesh in the scene. A Track can be used as well as a TrackIntegrator.

from track import *
from mesh import *
import numpy as np


class TrackMesh(Mesh):
    def __init__(self, track):

        semiWidth = .579225

        self.points = []
        self.segs = []
        self.tris = []

        n = track.lt - 2

        for i in range(n):
            a = track.points[i]
            b = track.points[i+1]
            c = track.points[i+2]
            tang = (c - a).normalized
            normal = (a+c-b*2).normalized

            # # no upside down
            # if normal.z <= 0:
            #     normal = -normal

            # For circular loop only
            if i <= 31 or 126 < i:
                normal = Vector3(0, 0, 1)

            lateral = (Vector3.cross(tang, normal)).normalized

            self.points.append(b+lateral*semiWidth)
            self.points.append(b-lateral*semiWidth)

        for i in range(n-2):
            self.segs.append([2*i, 2*i+2])
            self.segs.append([2*i+1, 2*i+3])
        for i in range(1, n-2):
            self.segs.append([2*i, 2*i+1])
