from track import *
from mesh import *
import numpy as np


# def autoLinspace(start, stop, pointsEvery1):
#     return np.linspace(start, stop, int(pointsEvery1 * np.abs(stop - start)))


class TrackMesh(Mesh):
    def __init__(self, track):

        semiWidth = .579225
        #ts = autoLinspace(track.tStart, track.tEnd, pointsEvery1)

        # self.points = track.points
        # #[track.function.evaluate(t) for t in track.ts]
        # self.segs = [[i, i + 1] for i in range(track.lt - 1)]
        # self.tris = []

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

            if i <= 7:
                normal = Vector3(0, 0, 1)

            # # print("normal", normal.normalized, "sqr module", normal.sqrModule)

            # # if normal.sqrModule <= .05 or .1 <= normal.sqrModule:
            # # .0075/.005
            # if normal.sqrModule <= .006 or i <= 20 or 80 <= i:
            #     normal = Vector3(0, 0, 1)
            # else:
            #     normal = normal.normalized
            # # print("modified normal", normal)

            lateral = (Vector3.cross(tang, normal)).normalized

            self.points.append(b+lateral*semiWidth)
            self.points.append(b-lateral*semiWidth)

        for i in range(n-2):
            self.segs.append([2*i, 2*i+2])
            self.segs.append([2*i+1, 2*i+3])
        for i in range(1, n-2):
            self.segs.append([2*i, 2*i+1])

        # n = track.lt - 4

        # for i in range(n):
        #     a = track.points[i]
        #     b = track.points[i+2]
        #     c = track.points[i+4]
        #     tang = (c - b).normalized
        #     normal = (a+c-b*2)

        #     print("normal sqr module", normal.sqrModule)

        #     if normal.sqrModule <= .05 or .1 <= normal.sqrModule:
        #         normal = Vector3(0, 0, 1)
        #     else:
        #         normal = normal.normalized

        #     lateral = (Vector3.cross(tang, normal)).normalized

        #     self.points.append(b+lateral*semiWidth)
        #     self.points.append(b-lateral*semiWidth)

        # for i in range(n-4):
        #     self.segs.append([2*i, 2*i+2])
        #     self.segs.append([2*i+1, 2*i+3])
        # for i in range(1, n-4):
        #     self.segs.append([2*i, 2*i+1])
