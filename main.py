import pygame as pg
import numpy as np

from camera import *
from color import *
from entity import *
from matrix2x2 import *
from mesh import *
from quaternion import *
# from segment2 import *
# from segment3 import *
from transform3 import *
from unit import *
from vector2 import *
from vector3 import *


def main():
    pg.init()
    pg.display.set_caption("Project Phoenix")

    inputCubeRotation = Vector3()
    inputCubePosition = 0
    inputPyramidRotation = 0
    inputPyramidScale = 0

    while True:
        for event in pg.event.get():

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

        update(inputCubeRotation*.02, inputCubePosition*.02,
               inputPyramidRotation*.02, inputPyramidScale*.02)

        Camera.Main.render()


def update(inputCubeRotation, inputCubePosition, inputPyramidRotation, inputPyramidScale):
    Box.transform.localPosRotScale3.rotation = Box.transform.localPosRotScale3.rotation.rotated(
        Quaternion.eulerToQuaternion(inputCubeRotation))

    Box.transform.localPosRotScale3.position += Vector3.right*inputCubePosition

    Pyramid.transform.localPosRotScale3.rotation = Pyramid.transform.localPosRotScale3.rotation.rotated(
        Quaternion.eulerToQuaternion(Vector3.up*inputPyramidRotation))

    Pyramid.transform.localPosRotScale3.scale += Vector3.one*inputPyramidScale


main()
