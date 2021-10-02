import numpy as np
import pygame as pg

from unit import *
from color import *
from space import *
from mesh import *
from meshRenderer import *
from utilities import *
from vectorRenderer import *


class Camera(Unit):

    def __init__(self, res=Vector2(1920, 1080), perspective=True, persScaler=.975, orthoSize=2, segs=True, tris=True, backgroundColor=Color.black):
        self.res = res
        self.perspective = perspective
        self.persScaler = persScaler
        self.orthoSize = orthoSize
        self.segs = segs
        self.tris = tris
        self.backgroundColor = backgroundColor
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

    @property
    def persScaler(self): return self._persScaler

    @persScaler.setter
    def persScaler(self, value):
        if 0 <= value <= 1:
            self._persScaler = value

    @property
    def orthoSize(self): return self._orthoSize

    @orthoSize.setter
    def orthoSize(self, value):
        if 0 <= value:
            self._orthoSize = value

    @property
    def ratio(self): return self.res.x / self.res.y

    @property
    def centre(self): return self.res / 2

    @property
    def renderSize(self): return self.orthoSize * self.res.y * .1

    def render(self):
        self.screen.fill(self.backgroundColor.toTuple())

        # camPosRotScale3 = self.transform.localPosRotScale3
        for meshRenderer in MeshRenderers:

            preRenderedPoints = [self.preRender(
                p) for p in meshRenderer.globalPoints()]
            # preRenderedPoints = self.batchPreRender(meshRenderer.globalPoints())

            if self.tris:
                for tri in meshRenderer.mesh.tris:
                    self.drawTri([preRenderedPoints[tri[k]].toTuple()
                                  for k in range(3)])

            if self.segs:
                for seg in meshRenderer.mesh.segs:
                    self.drawSeg([preRenderedPoints[seg[k]]
                                  for k in range(2)])

        # print(PosRotScale3.relativePos(
        #     Vector3(0, 0, 5), self.transform.globalPosRotScale3))

        # self.drawSeg([self.preRender(Vector3(0, 0, 5)),
        #               self.preRender(Vector3(0, 2, 5))], Color.magenta)
        for vectorRenderer in VectorRenderers:
            # print(vectorRenderer.vectorPoints[0])
            # print(vectorRenderer.vectorPoints[1])
            # print(vectorRenderer.vectorPoints[1] -
            #       vectorRenderer.vectorPoints[0])

            # print(PosRotScale3.relativePos(
            #     vectorRenderer.vectorPoints[1], self.transform.globalPosRotScale3)-PosRotScale3.relativePos(
            #     vectorRenderer.vectorPoints[0], self.transform.globalPosRotScale3))

            # self.drawSeg(
            #     [(self.centre + vectorRenderer.vectorPoints[0].toVector2 * (self.persScaler**(-vectorRenderer.vectorPoints[0].z) if self.perspective else 1) * self.renderSize), (self.centre + vectorRenderer.vectorPoints[1].toVector2 * (self.persScaler**(-vectorRenderer.vectorPoints[1].z) if self.perspective else 1) * self.renderSize)], vectorRenderer.color)
            self.drawSeg([self.preRender(vectorRenderer.vectorPoints[0]), self.preRender(
                vectorRenderer.vectorPoints[1])], vectorRenderer.color)
            # self.drawSeg([self.preRender(PosRotScale3.relativePos(
            #     vectorRenderer.vectorPoints[0], Transform3Master.Master.globalPosRotScale3)), self.preRender(PosRotScale3.relativePos(
            #         vectorRenderer.vectorPoints[1], Transform3Master.Master.globalPosRotScale3))], vectorRenderer.color)

        origin = False
        if origin:
            #     preRenderedPoints = self.batchPreRender(
            #         [Vector3(0, 0, 0), Vector3(1, 0, 0), Vector3(0, 1, 0), Vector3(0, 0, 1)])

            preRenderedPoints = [self.preRender(PosRotScale3.relativePos(axisPoint, Transform3Master.Master.localPosRotScale3)) for axisPoint in [
                Vector3.zero, Vector3.right, Vector3.forward, Vector3.up]]

            # preRenderedPoints = self.batchPreRender([PosRotScale3.relativePos(axisPoint, Transform3Master.Master.localPosRotScale3) for axisPoint in [Vector3.zero, Vector3.right, Vector3.forward, Vector3.up]])
            colors = [Color.red, Color.green, Color.blue]
            # for k in preRenderedPoints:
            #     print(k)
            for k in range(3):
                self.drawSeg(
                    [preRenderedPoints[0], preRenderedPoints[k + 1]], colors[k])

        pg.display.update()

    def preRender(self, point):
        relativePoint = PosRotScale3.relativePos(
            point, self.transform.globalPosRotScale3)

        # relativePoint = PosRotScale3.relative(
        #     PosRotScale3(point), self.transform.globalPosRotScale3()).position
        return self.centre + relativePoint.toVector2 * (self.persScaler**(-relativePoint.z) if self.perspective else 1) * self.renderSize
        # return self.centre + relativePoint.toVector2 * (np.exp(self.persScaler * relativePoint.z) if self.perspective else 1) * self.renderSize

    # def batchPreRender(self, points):
    #     preRenderedPoints = []
    #     for point in points:
    #         preRenderedPoints.append(self.preRender(point))
    #     return preRenderedPoints

    def drawSeg(self, seg, color=Color.white): pg.draw.line(
        self.screen, color.toTuple(False), seg[0].toTuple(), seg[1].toTuple(), 5)

    def drawTri(self, tri, color=Color.grey):
        # print(tri)
        pg.draw.polygon(
            self.screen, color.toTuple(False), tri)

    def __str__(self):
        return ("Perspective" if self.perspective else "Orthographic") + " camera"


Camera.Main = Camera()
