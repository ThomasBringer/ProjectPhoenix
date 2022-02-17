from numpy.core.arrayprint import _get_format_function
from clock import *
from physics import *
from unit import *

import numpy as np
import pygame as pg

from space import *

import matplotlib.pyplot as plt

from function3 import *


class TrackBody(UpdatableUnit):

    # , speedVectorRenderer, accelerationVectorRenderer, gForceVectorRenderer):
    def __init__(self, track, accelerationVectorRenderer, trackPos):
        self.track = track
        # self.speedVectorRenderer = speedVectorRenderer
        self.accelerationVectorRenderer = accelerationVectorRenderer
        # self.gForceVectorRenderer = gForceVectorRenderer
        self.trackPos = trackPos
        self.d = 0
        self.heightVar = 0
        self.lastSpeedVector = Vector3.forward * 25  # .0001
        self.originalHeight = track.start.z
        self.t = 0
        self.ts = []
        self.speeds = []
        self.accelerations = []
        self.gForces = []
        self.lastDeltaTime = deltaTime()

    # Uses conservation energy to compute speed, depending on the variation of height. v²=v_0^2 - 2g deltaH

    def calcSqrSpeed(self):
        # print("lastSqrSpeed", self.lastSpeedVector.sqrModule, "heightVar (before)",
        #       self.heightVar, "...", self.lastSpeedVector.sqrModule - 2 * g * self.heightVar)
        return self.lastSpeedVector.sqrModule - 2 * g * self.heightVar
        # if self.heightVar < 0:
        #     return np.sqrt(self.lastSpeedVector.sqrModule - 2 * g * self.heightVar)
        # else:
        #     return self.lastSpeedVector.module

    # Uses Menger Curvature to compute the radius or a circle, using three points on the circle. r=2sin(abc)/|a-c|
    def mengerRadius(self, a, b, c):
        # print("a", a, "b", b, "c", c)
        s = Vector3.sinAngleBetween(a-b, c-b)
        return 0 if s == 0 else Vector3.distance(a, c)/(2*s)
        # return 2*(Vector3).sinAngleBetween(a-b, c-b)/Vector3.distance(a, c)

    # Uses deivatives ton compute the curvature radius. r = |f'|**3/|f' ^ f''|
    def derivativeRadius(self, t):
        der1 = Function3.CircleLoopDer1
        der2 = Function3.CircleLoopDer2
        der1t = der1.evaluate(t)
        der2t = der2.evaluate(t)
        return ((der1t.module)**3)/((Vector3.cross(der1t, der2t)).module)
        # def mengerCurvature(self, a, b, c):
        #     r = self.mengerRadius(a, b, c)
        #     return np.infty if r == 0 else 1/r

    def update(self):
        a = self.getPos(self.D - 1)
        b = self.getPos(self.D)
        c = self.getPos(self.D + 1)

        dt = deltaTime()
        tang = (c - a).normalized
        normal = (a+c-b*2).normalized

        if self.D <= 7:
            normal = Vector3(0, 0, 1)

        # # print("normal", normal)
        # # or ((normal.normalized-Vector3(x=-0.9998901017408137, y=0.014821386790648846, z=0.00033306808186257407)).sqrModule < .1 and not done):
        # if normal.sqrModule < .006 or self.D <= 7 or 80 <= self.D:
        #     normal = Vector3(0, 0, 1)
        #     # if((normal.normalized-Vector3(x=-0.9998901017408137, y=0.014821386790648846, z=0.00033306808186257407)).sqrModule < .01):
        #     #     done = True
        # else:
        #     normal = normal.normalized

        # print("dir", dir)

        sqrSpeed = self.calcSqrSpeed()
        speed = np.sqrt(sqrSpeed)
        speedVector = tang*speed
        # self.speedVectorRenderer.vector = speedVector

        dist = speed * dt

        # # # # # acceleration = (speed - self.lastSpeed) / self.lastDeltaTime

        # a=v²/r

        r = self.mengerRadius(a, b, c)
        # r = self.mengerRadius(a, b, c)
        # print("r", r)
        # print("tang", tang)
        if r == 0:
            acceleration = 0
        else:
            acceleration = sqrSpeed/r

        # acceleration = 0 if r == 0 else sqrSpeed*self.mengerCurvature(a, b, c)
        accelerationVector = normal * acceleration
        # accelerationVector = (speedVector-self.lastSpeedVector)

        self.accelerationVectorRenderer.vector = accelerationVector
        gForce = Vector3.up+accelerationVector/g
        # self.gForceVectorRenderer.vector = gForce

        # print("gForce:", gVect-accelerationVector)
        # print("gForceVector:", self.gForceVectorRenderer.vector)

        # acceleration = accelerationVector.module

        self.ts.append(self.t)
        self.t += dt
        self.speeds.append(speed)
        self.accelerations.append(acceleration)
        self.gForces.append(gForce.module)
        self.lastDeltaTime = dt

        self.heightVar = tang.z * dist
        self.lastSpeedVector = speedVector

        self.D += dist

        # ,"", self.track.DistToT(dist))
        # print("heightVar", self.heightVar, "speed", speed, "dist", dist)
        # print("dist:", dist)

        self.transform.localPosRotScale3.rotation.face(tang, normal)

        print()

        # self.transform.localPosRotScale3.rotation.localForward = tang

    @ property
    def D(self):
        return self.d

    @ D.setter
    def D(self, value):
        self.tryTerminate(value)

        self.applyPos(value)
        self.d = value

    def getPos(self, d):
        self.tryTerminate(d)
        return self.track.FakeCurve(d)

    def applyPos(self, d):
        self.transform.localPosRotScale3.position = self.getPos(
            d) + self.trackPos

    def tryTerminate(self, dValue):
        if dValue >= self.track.maxDist:
            self.terminate()

    def terminate(self):
        self.ts.pop()
        self.ts.pop()
        self.ts.pop(0)
        self.ts.pop(0)
        self.gForces.pop()
        self.gForces.pop()
        self.gForces.pop(0)
        self.gForces.pop(0)

        # ts = np.linspace(0, 1, len(self.gForces))
        # plt.plot(ts, self.speeds)
        # plt.plot(ts, self.accelerations)

        plt.plot(self.ts, self.gForces)
        plt.xlabel("temps (secondes)")
        plt.ylabel("G-force (g)")
        plt.ylim([0, 8])
        plt.show()
        exit()
