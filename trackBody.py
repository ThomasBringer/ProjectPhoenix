from clock import *
from physics import *
from unit import *

import numpy as np
import pygame as pg

from space import *

import matplotlib.pyplot as plt


class TrackBody(UpdatableUnit):

    def __init__(self, track, speedVectorRenderer, accelerationVectorRenderer, gForceVectorRenderer):
        self.track = track
        self.speedVectorRenderer = speedVectorRenderer
        self.accelerationVectorRenderer = accelerationVectorRenderer
        self.gForceVectorRenderer = gForceVectorRenderer
        self.d = 0
        self.heightVar = 0
        self.lastSpeedVector = Vector3.forward * .0001
        self.originalHeight = track.start.z
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

    # def mengerCurvature(self, a, b, c):
    #     r = self.mengerRadius(a, b, c)
    #     return np.infty if r == 0 else 1/r

    def update(self):
        a = self.getPos(self.D - 1)
        b = self.getPos(self.D)
        c = self.getPos(self.D + 1)
        dt = deltaTime()

        dir = (c - b).normalized
        tang = (a+c-b*2).normalized
        # print("dir", dir)

        sqrSpeed = self.calcSqrSpeed()
        speed = np.sqrt(sqrSpeed)
        speedVector = dir*speed
        self.speedVectorRenderer.vector = speedVector

        dist = speed * dt

        # # # # # acceleration = (speed - self.lastSpeed) / self.lastDeltaTime

        # a=v²/r
        r = self.mengerRadius(a, b, c)
        # print("r", r)
        # print("tang", tang)
        if r == 0:
            acceleration = 0
        else:
            acceleration = sqrSpeed/r

        # acceleration = 0 if r == 0 else sqrSpeed*self.mengerCurvature(a, b, c)
        accelerationVector = tang * acceleration
        # accelerationVector = (speedVector-self.lastSpeedVector)

        self.accelerationVectorRenderer.vector = accelerationVector
        gForce = gVect-accelerationVector
        self.gForceVectorRenderer.vector = gForce

        # print("gForce:", gVect-accelerationVector)
        # print("gForceVector:", self.gForceVectorRenderer.vector)

        # acceleration = accelerationVector.module

        self.speeds.append(speed)
        self.accelerations.append(acceleration)
        self.gForces.append(gForce.module)
        self.lastDeltaTime = dt

        self.heightVar = dir.z * dist
        self.lastSpeedVector = speedVector

        self.D += dist

        # ,"", self.track.DistToT(dist))
        # print("heightVar", self.heightVar, "speed", speed, "dist", dist)
        # print("dist:", dist)

        self.transform.localPosRotScale3.rotation.localForward = dir

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
        self.transform.localPosRotScale3.position = self.getPos(d)

    def tryTerminate(self, dValue):
        if dValue >= self.track.maxDist:
            self.terminate()

    def terminate(self):
        ts = np.linspace(0, 1, len(self.speeds))
        plt.plot(ts, self.speeds)
        plt.plot(ts, self.accelerations)
        plt.plot(ts, self.gForces)
        plt.show()
        exit()
