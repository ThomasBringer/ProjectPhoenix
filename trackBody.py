from clock import *
from physics import *
from unit import *

import numpy as np
import pygame as pg

from space import *

import matplotlib.pyplot as plt


class TrackBody(UpdatableUnit):
    def __init__(self, track, speedVectorRenderer, accelerationVectorRenderer):
        self.track = track
        self.speedVectorRenderer = speedVectorRenderer
        self.accelerationVectorRenderer = accelerationVectorRenderer
        self.t = track.tStart
        self.heightVar = 0
        self.lastSpeedVector = Vector3.forward*.0001
        self.originalHeight = track.start.z
        self.speeds = []
        self.accelerations = []
        self.lastDeltaTime = deltaTime()
#         self.transform.posRotScale3.position = track.points[0]
#         self.originalHeight = self.transform.posRotScale3.position.z+1

    # @property def tangentSpeed(self):
    # return np.sqrt(2*g*(originalHeight-self.transform.localPosRotScale3.position.z))

    # speed=lambda lastSpeed,heightVar:np.sqrt(lastSpeed**2 - 2 * g * self.heightVar)

    def calcSpeed(self):
        return np.sqrt(self.lastSpeedVector.sqrModule - 2 * g * self.heightVar)
        # sqrSpeed = self.lastSpeed**2 - 2 * g * self.heightVar
        # return np.sign(sqrSpeed) * np.sqrt(np.abs(sqrSpeed))

    def update(self):

        if self.T >= self.track.tEnd:
            # ts = np.linspace(0, 1, len(self.speeds))
            # plt.plot(ts, self.speeds)
            # plt.plot(ts, self.accelerations)
            # plt.show()
            # exit()
            return

        dir = (self.getPos(self.T + .1) -
               self.getPos(self.T)).normalized

        speed = self.calcSpeed()
        speedVector = dir*speed
        self.speedVectorRenderer.vector = speedVector

        dist = speed * deltaTime()

        self.speeds.append(speed)
        # acceleration = (speed - self.lastSpeed) / self.lastDeltaTime

        accelerationVector = (speedVector-self.lastSpeedVector)*5
        self.accelerationVectorRenderer.vector = accelerationVector

        acceleration = accelerationVector.module

        self.accelerations.append(acceleration)
        self.lastDeltaTime = deltaTime()

        self.heightVar = dir.z * dist
        self.lastSpeedVector = speedVector

        self.T += dist

        self.transform.localPosRotScale3.rotation.localForward = dir

    # def update(self):

    #     if self.T >= self.track.tEnd:
    #         # ts = np.linspace(0, 1, len(self.speeds))
    #         # plt.plot(ts, self.speeds)
    #         # plt.plot(ts, self.accelerations)
    #         # plt.show()
    #         # exit()
    #         return

    #     dir = (self.getPos(self.T + .1) -
    #            self.getPos(self.T)).normalized
    #     # dir = Vector3(dir.x, dir.x, dir.z)
    #     # print(dir)

    #     # dir = (self.getPos(self.T + .1) -
    #     #        self.transform.localPosRotScale3.position).normalized

    #     speed = self.calcSpeed()

    #     # u = self.transform.localPosRotScale3.rotation.localForward
    #     self.speedVectorRenderer.vector = dir*speed

    #     # speed = np.sqrt(self.lastSpeed**2 - 2 * g * self.heightVar)
    #     #print("heightVar", self.heightVar, "2 * g * heightVar", (2 * g * self.heightVar), "lastSpeed", self.lastSpeed, "speed", speed)
    #     dist = speed * deltaTime()

    #     self.speeds.append(speed)
    #     # acceleration = (speed - self.lastSpeed) / self.lastDeltaTime
    #     self.accelerations.append(acceleration)
    #     self.lastDeltaTime = deltaTime()
    #     # print(deltaTime())
    #     self.heightVar = dir.z * dist
    #     self.lastSpeed = speed
    #     # print(speed)
    #     self.T += dist

    #     self.transform.localPosRotScale3.rotation.localForward = dir
    #     # print(self.transform.localPosRotScale3.rotation.localForward)

    #     # print(dir)
    #     # print(self.transform.localPosRotScale3.rotation.localForward)

    #     #print("clck0.get_time(): ", clck0.get_time())
    #     # self.transform.localPosRotScale3.translate(dir * dist)

    #     # dir = (self.track.end - self.track.start).normalized()
    #     # dist = np.sqrt(2 * g * (self.originalHeight -
    #     #                         self.transform.localPosRotScale3.position.z)) * time()
    #     # # z=dir.z*dist
    #     # self.T += dist

    @property
    def T(self): return self.t

    @T.setter
    def T(self, value):
        self.applyPos(value)
        self.t = value

    def getPos(self, t):
        track = self.track
        return Vector3(track.xt(t), track.yt(t), track.zt(t))

    def applyPos(self, t):
        self.transform.localPosRotScale3.position = self.getPos(t)
