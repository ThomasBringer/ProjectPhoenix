# A Camera is a Unit responsible for drawing objects on the canvas. A virtual camera that can attached to an Entity.

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

    def __init__(self, res=Vector2(1920, 1080), perspective=True, persScaler=.975, orthoSize=2, segs=True, tris=True, backgroundColor=Color.white):
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

    # Size of the orthographic camera.
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

    # Renders all objects on the canvas.
    def render(self):
        self.screen.fill(self.backgroundColor.toTuple())

        for meshRenderer in MeshRenderers:  # Loop through mesh renderers:

            # Projects point on the 2D canvas.
            preRenderedPoints = [self.preRender(
                p) for p in meshRenderer.globalPoints()]

            # Renders all triangles.
            if self.tris:
                for tri in meshRenderer.mesh.tris:
                    self.drawTri([preRenderedPoints[tri[k]].toTuple()
                                  for k in range(3)], meshRenderer.triColor)

            # Renders all segments.
            if self.segs:
                for seg in meshRenderer.mesh.segs:
                    self.drawSeg([preRenderedPoints[seg[k]]
                                  for k in range(2)], meshRenderer.segColor)

        # Render all vector renderers.
        for vectorRenderer in VectorRenderers:
            self.drawSeg([self.preRender(vectorRenderer.vectorPoints[0]), self.preRender(
                vectorRenderer.vectorPoints[1])], vectorRenderer.color)

        # Renders the origin.
        origin = False
        if origin:
            preRenderedPoints = [self.preRender(PosRotScale3.relativePos(axisPoint, Transform3Master.Master.localPosRotScale3)) for axisPoint in [
                Vector3.zero, Vector3.right, Vector3.forward, Vector3.up]]

            colors = [Color.red, Color.green, Color.blue]

            for k in range(3):
                self.drawSeg(
                    [preRenderedPoints[0], preRenderedPoints[k + 1]], colors[k])

        pg.display.update()

    # Computes the projection of a 3D position onto the 2D canvas of the screen.
    def preRender(self, point):
        relativePoint = PosRotScale3.relativePos(
            point, self.transform.globalPosRotScale3)
        return self.centre + relativePoint.toVector2 * (self.persScaler**(-relativePoint.z) if self.perspective else 1) * self.renderSize

    # Draws a segment on the canvas.
    def drawSeg(self, seg, color=Color.white): pg.draw.line(
        self.screen, color.toTuple(False), seg[0].toTuple(), seg[1].toTuple(), 5)

    # Draws a triangle on the canvas.
    def drawTri(self, tri, color=Color.grey):
        pg.draw.polygon(
            self.screen, color.toTuple(False), tri)

    def __str__(self):
        return ("Perspective" if self.perspective else "Orthographic") + " camera"


Camera.Main = Camera()
