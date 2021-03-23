# test new

import pygame as pg
import numpy as np

from camera import *
from color import *
from entity import *
from matrix2x2 import *
from mesh import *
from quaternion import *
from segment2 import *
from segment3 import *
from transform3 import *
from unit import *
from vector2 import *
from vector3 import *


# print([str(i) for i in [Vector3(0, 1, 0), 1, Color(255, 0, 255, 1)]])
# print(str([Vector3(0, 1, 0), 1, Color(255, 0, 255, 1)]))


# seg = Segment3(Vector3.zero, Vector3.one)
# print(seg)
# print(seg.length())
# print(seg.middle())


# print(Transform3Master.Master)
# print(len(Transform3Master.Master.children),
#       Transform3Master.Master.children[0])
# print(Entity.Cube.transform.parent)
# print(Entity.Cube.transform)
# print(len(Entity.Cube.transform.children), Entity.Cube.transform.children[0])
# print(Entity.Pyramid.transform.parent)
# print(Entity.Pyramid.transform)
# print(len(Entity.Pyramid.transform.children))


def main():
    pg.init()

    pg.display.set_caption("Project Phoenix")

    inputCubeRotation = Vector3()
    inputCubePosition = 0
    inputPyramidRotation = 0
    inputPyramidScale = 0

    while True:
        for event in pg.event.get():
            # keys = pg.key.get_pressed()

            # input.x = -1 if K_LEFT in keys else (1 if K_RIGHT in keys else 0)
            # input.y = -1 if K_DOWN in keys else (1 if K_UP in keys else 0)
            # input.x = -1 if keys[K_LEFT] else (1 if keys[K_RIGHT] else 0)
            # input.y = -1 if keys[K_DOWN] else (1 if keys[K_UP] else 0)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    inputCubeRotation.y = -1
                elif event.key == pg.K_RIGHT:
                    inputCubeRotation.y = 1
                if event.key == pg.K_DOWN:
                    inputCubeRotation.x = -1
                elif event.key == pg.K_UP:
                    inputCubeRotation.x = 1
                if event.key == pg.K_w:
                    inputCubeRotation.z = -1
                elif event.key == pg.K_x:
                    inputCubeRotation.z = 1
                if event.key == pg.K_q:
                    inputPyramidRotation = -1
                elif event.key == pg.K_s:
                    inputPyramidRotation = 1
                if event.key == pg.K_a:
                    inputPyramidScale = -1
                elif event.key == pg.K_z:
                    inputPyramidScale = 1
                if event.key == pg.K_c:
                    inputCubePosition = -1
                elif event.key == pg.K_v:
                    inputCubePosition = 1
            elif event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    inputCubeRotation.y = 0
                if event.key == pg.K_DOWN or event.key == pg.K_UP:
                    inputCubeRotation.x = 0
                if event.key == pg.K_w or event.key == pg.K_x:
                    inputCubeRotation.z = 0
                if event.key == pg.K_q or event.key == pg.K_s:
                    inputPyramidRotation = 0
                if event.key == pg.K_a or event.key == pg.K_z:
                    inputPyramidScale = 0
                if event.key == pg.K_c or event.key == pg.K_v:
                    inputCubePosition = 0
            if event.type == pg.QUIT:
                pg.quit()

        update(inputCubeRotation*.005, inputCubePosition*.005,
               inputPyramidRotation*.005, inputPyramidScale*.005)

        Camera.Main.render()


def update(inputCubeRotation, inputCubePosition, inputPyramidRotation, inputPyramidScale):
    Box.transform.localPosRotScale3.rotation = Box.transform.localPosRotScale3.rotation.rotated(
        Quaternion.eulerToQuaternion(inputCubeRotation))

    Box.transform.localPosRotScale3.position += Vector3.right*inputCubePosition

    # print(Box.transform.localPosRotScale3.rotation)
    # print(Pyramid.transform.parent)

    Pyramid.transform.localPosRotScale3.rotation = Pyramid.transform.localPosRotScale3.rotation.rotated(
        Quaternion.eulerToQuaternion(Vector3.up*inputPyramidRotation))

    Pyramid.transform.localPosRotScale3.scale += Vector3.one*inputPyramidScale

    # Cube.transform.localPosRotScale3.rotation = Cube.transform.localPosRotScale3.rotation.rotated(
    #     Quaternion.eulerToQuaternion(inputCubeRotation))

    # Cube.transform.localPosRotScale3.rotation = Cube.transform.localPosRotScale3.rotation.rotated(
    #     Quaternion.angleAxis(input.x, Vector3.forward))
    # Cube.transform.localPosRotScale3.rotation = Cube.transform.localPosRotScale3.rotation.rotated(
    #     Quaternion.angleAxis(input.y, Vector3.right))
    # Cube.transform.localPosRotScale3.rotation = Cube.transform.localPosRotScale3.rotation.rotated(
    #     Quaternion.angleAxis(input.z, Vector3.up))


main()
