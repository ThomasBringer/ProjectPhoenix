# A Unit managing the physics of a cart on a roller coaster track.
# TrackBody updates the Transform3 position of the attached Entity to react to physics while staying on the track.

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

    def __init__(self, track, accelerationVectorRenderer, trackPos):
        self.track = track
        self.accelerationVectorRenderer = accelerationVectorRenderer
        self.trackPos = trackPos
        self.d = 0
        self.heightVar = 0
        self.lastSpeedVector = Vector3.forward * 25
        self.originalHeight = track.start.z
        self.t = 0
        self.ts = []
        self.speeds = []
        self.accelerations = []
        self.gForces = []
        self.lastDeltaTime = deltaTime()

    # Uses Menger curvature to compute the radius of a circle, using three points on the circle. r=2sin(abc)/|a-c|

    def mengerRadius(self, a, b, c):
        s = Vector3.sinAngleBetween(a-b, c-b)
        return 0 if s == 0 else Vector3.distance(a, c)/(2*s)

    # Unused. Uses derivatives to compute the curvature radius. r = |f'|**3/|f' ^ f''|
    def derivativeRadius(self, t):
        der1 = Function3.CircleLoopDer1
        der2 = Function3.CircleLoopDer2
        der1t = der1.evaluate(t)
        der2t = der2.evaluate(t)
        return ((der1t.module)**3)/((Vector3.cross(der1t, der2t)).module)

    # Updates position to react to physics.
    def update(self):
        # Position right before.
        a = self.getPos(self.D - self.track.sampleDist)
        b = self.getPos(self.D)  # Current position.
        # Position right after.
        c = self.getPos(self.D + self.track.sampleDist)

        dt = deltaTime()
        tang = (c - a).normalized  # Tangent direction.
        normal = (a+c-b*2).normalized  # Normal direction.

        # Uses conservation energy to compute speed, depending on the variation of height. v²(t + dt) = v(t)^2 - 2g dh
        sqrSpeed = self.lastSpeedVector.sqrModule - \
            2 * g * self.heightVar  # (1 - fric*dt)*

        speed = np.sqrt(sqrSpeed)
        speedVector = tang*speed

        dist = speed * dt

        # Computes the curvature of the track to find normal acceleration.
        r = self.mengerRadius(a, b, c)

        if r == 0:
            acceleration = 0
        else:
            acceleration = sqrSpeed/r

        accelerationVector = normal * acceleration

        self.accelerationVectorRenderer.vector = accelerationVector
        gForce = Vector3.up+accelerationVector/g

        self.ts.append(self.t)
        self.t += dt
        self.speeds.append(speed)
        self.accelerations.append(acceleration)
        self.gForces.append(gForce.module)
        self.lastDeltaTime = dt

        self.heightVar = tang.z * dist
        self.lastSpeedVector = speedVector

        self.D += dist

        # # no upside down
        # if normal.z <= 0:
        #     normal = -normal
        # Updates rotation of the cart.
        self.transform.localPosRotScale3.rotation.face(tang, normal)

    # Curvilinear abscissa along the track.

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
        return self.track.AffineCurve(d)

    def applyPos(self, d):
        self.transform.localPosRotScale3.position = self.getPos(
            d) + self.trackPos

    def tryTerminate(self, dValue):
        if dValue >= self.track.maxDist:
            self.terminate()

    # Ends simulation and displays a graph of G-forces.
    def terminate(self):
        plt.plot(self.ts, self.gForces)
        plt.xlabel("temps (secondes)")
        plt.ylabel("G-force (g)")
        plt.ylim([0, 8])
        plt.show()
        exit()
