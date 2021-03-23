import numpy as np
import pygame as pg

from unit import *
from color import *
from vector2 import *
from vector3 import *
from mesh import *
from utilities import *


class Camera(Unit):

    def __init__(self, res=Vector2(1920, 1080), perspective=True, persScaler=.5, orthoSize=2, segs=True, tris=True, backgroundColor=Color.black):
        self.res = res
        self.perspective = perspective
        self.persScaler = persScaler
        self.orthoSize = orthoSize
        self.segs = segs
        self.tris = tris
        self.backgroundColor = backgroundColor
        self.screen = pg.display.set_mode(self.res.toTuple())
        self.centre = self.res/2
        self.renderSize = orthoSize*res.y*.1

    def ratio(self):
        return self.res.x/self.res.y

    def render(self):
        self.screen.fill(self.backgroundColor.toTuple())

        camPosRotScale3 = self.transform.localPosRotScale3
        for thisMesh in Meshes:

            points = []
            for point in thisMesh.globalPoints():
                relativePoint = PosRotScale3.relativePos(
                    point, camPosRotScale3)
                points.append(self.centre+relativePoint.toVector2()*(np.exp(
                    self.persScaler*relativePoint.z) if self.perspective else 1) * self.renderSize)

            if self.tris:
                for tri in thisMesh.tris:
                    self.drawTri([points[tri[k]].toTuple() for k in range(3)])

            if self.segs:
                for seg in thisMesh.segs:
                    self.drawSeg([points[seg[k]].toTuple() for k in range(2)])

        pg.display.update()

    def drawSeg(self, seg): pg.draw.line(
        self.screen, Color.red.toTuple(False), seg[0], seg[1], 5)

    def drawTri(self, tri): pg.draw.polygon(
        self.screen, Color.white.toTuple(False), tri)

    def __str__(self):
        return ("Perspective" if self.perspective else "Orthographic")+" camera"


Camera.Main = Camera()
