from clock import *
from physics import *
from unit import *

import numpy as np
import pygame as pg

from vector3 import *

import matplotlib.pyplot as plt


class TrackBody(UpdatableUnit):
    def __init__(self, track):
        self.track = track
        self.t = track.tStart
        self.heightVar = 0
        self.lastSpeed = .0001
        self.originalHeight = track.start.z + 1
        self.speeds = []
        self.accelerations = []
        self.lastDeltaTime = deltaTime()
#         self.transform.posRotScale3.position = track.points[0]
#         self.originalHeight = self.transform.posRotScale3.position.z+1

    # @property def tangentSpeed(self):
    # return np.sqrt(2*g*(originalHeight-self.transform.localPosRotScale3.position.z))

    # speed=lambda lastSpeed,heightVar:np.sqrt(lastSpeed**2 - 2 * g * self.heightVar)

    def calcSpeed(self):
        return np.sqrt(self.lastSpeed**2 - 2 * g * self.heightVar)
        # sqrSpeed = self.lastSpeed**2 - 2 * g * self.heightVar
        # return np.sign(sqrSpeed) * np.sqrt(np.abs(sqrSpeed))

    def update(self):

        if self.T >= self.track.tEnd:
            ts = np.linspace(0, 1, len(self.speeds))
            plt.plot(ts, self.speeds)
            plt.plot(ts, self.accelerations)
            plt.show()
            exit()
            return

        dir = (self.getPos(self.T + .1) -
               self.transform.localPosRotScale3.position).normalized

        speed = self.calcSpeed()
        # speed = np.sqrt(self.lastSpeed**2 - 2 * g * self.heightVar)
        #print("heightVar", self.heightVar, "2 * g * heightVar", (2 * g * self.heightVar), "lastSpeed", self.lastSpeed, "speed", speed)
        dist = speed * deltaTime()

        self.speeds.append(speed)
        acceleration = (speed - self.lastSpeed) / self.lastDeltaTime
        self.accelerations.append(acceleration)
        self.lastDeltaTime = deltaTime()
        # print(deltaTime())
        self.heightVar = dir.z * dist
        self.lastSpeed = speed
        # print(speed)
        self.T += dist

        self.transform.localPosRotScale3.rotation.localForward = dir

        #print("clck0.get_time(): ", clck0.get_time())
        # self.transform.localPosRotScale3.translate(dir * dist)

        # dir = (self.track.end - self.track.start).normalized()
        # dist = np.sqrt(2 * g * (self.originalHeight -
        #                         self.transform.localPosRotScale3.position.z)) * time()
        # # z=dir.z*dist
        # self.T += dist

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
