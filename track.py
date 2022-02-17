from numpy.lib.function_base import append
from utilities import *
from space import *
from function3 import *


class Track:

    def __init__(self, function, sampleDist=1):  # ,tilts
        self.function = function
        # self.tilts=tilts
        self.sampleDist = sampleDist
        self.start = self.function.start
        self.ts = self.sample()
        # print(sampleDist)
        # print(self.ts)
        self.lt = len(self.ts)
        self.maxDist = (self.lt-1)*sampleDist
        self.step = 1/(self.lt*self.sampleDist)
        sampledPoints = [self.function.evaluate(t) for t in self.ts]
        segLengths = [Vector.distance(
            sampledPoints[i], sampledPoints[i+1]) for i in range(self.lt-1)]
        # print("hey", segLengths)

    # eps=.0001, tryT=.01):
    def sample(self, eps=.5):
        t = self.function.tStart
        # print("start", t)
        ts = [t]
        self.points = [self.function.evaluate(t)]
        # firstStep = (self.function.tEnd-self.function.tStart)*.5
        a = 0

        step = eps*.1
        while True:
            last = ts[-1]
            t = (last+self.function.tEnd)*.5
            step = (self.function.tEnd-last)*.5
            # print("last", ts[-1], "new t:", t)
            dist = Vector3.distance(self.function.evaluate(
                ts[-1]), self.function.evaluate(t))

            a += 1
            if a >= 1000:
                exit()

            b = 0

            while eps < np.abs(dist - self.sampleDist) or t < last:

                b += 1
                if b >= 1000:
                    exit()

                step *= .5
                if self.sampleDist < dist and last < t:
                    t -= step
                    # if(t <= last):
                    #     t = last
                else:
                    t += step
                    # if(t >= self.function.tEnd):
                    #     t = self.function.tEnd
                dist = Vector3.distance(self.function.evaluate(
                    ts[-1]), self.function.evaluate(t))
                # print("t:", t,
                #       "evaluate(ts[-1])", self.function.evaluate(ts[-1]),
                #       "evaluate(t)", self.function.evaluate(t),

                #       "dist", dist, "step",
                #       step, "diff", dist - sampleDist)

            ts.append(t)
            self.points.append(self.function.evaluate(t))
            if Vector3.distance(self.function.evaluate(self.function.tEnd), self.function.evaluate(t)) <= self.sampleDist+eps:
                ts.append(self.function.tEnd)
                self.points.append(self.function.evaluate(t))
                return ts

    # # eps=.0001, tryT=.01):
    # def sample(self, sampleDist, eps=.5, tryT=.1):
    #     t = self.function.tStart
    #     ts = [t]
    #     while True:
    #         i = 1
    #         t += tryT

    #         if self.function.tEnd < t:
    #             return ts

    #         # print("0")
    #         # print("evaluate", self.function.evaluate(ts[-1]))
    #         # print("1")
    #         # print("ts-1", ts[-1])

    #         diff = Vector.distance(self.function.evaluate(
    #             ts[-1]), self.function.evaluate(t)) - sampleDist
    #         while eps < np.abs(diff):
    #             print("t", t, "diff", diff)
    #             t -= np.sign(diff)*tryT*(.5**i)
    #             if self.function.tEnd < t:
    #                 return ts
    #             i += 1
    #             diff = Vector.distance(self.function.evaluate(
    #                 ts[-1]), self.function.evaluate(t)) - sampleDist
    #         ts.append(t)

    def Lerp2Points(self, point1, point2, t):
        return point1+(point2-point1)*t

    def FakeCurve(self, dist):
        if dist <= 0:
            return self.start
        if dist >= self.maxDist:
            return self.end

        d = 0
        i = 0
        while d <= dist-1:
            d += self.sampleDist
            i += 1
        return self.Lerp2Points(self.points[i], self.points[i+1], dist-d)

    # def FakeCurve(self, dist):
    #     if dist <= 0:
    #         return self.function.start
    #     if dist >= self.maxDist:
    #         return self.end

    #     d = 0
    #     i = 0
    #     while d <= dist-1:
    #         d += self.sampleDist
    #         i += 1
    #     return self.Lerp2Points(self.function.evaluate(self.ts[i]), self.function.evaluate(self.ts[i+1]), dist-d)

    def TToDist(self, t):
        ti = 0
        i = 0
        dist = 0
        while ti <= t:
            dist += self.segLengths[i]
            i += 1
            ti += self.step
            # print(ti, t)
        dist += ((self.step-(ti-t))/self.step)*self.segLengths[i]
        return dist


Track.CircleLoop = Track(Function3.CircleLoop)
Track.Line = Track(Function3.Line)
