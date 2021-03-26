import pygame as pg
import sys
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


stateITRE = 0  # 0: idle, 1: translate, 2: rotate, 3: scalate
stateAxis = Vector3()


def main():
    pg.init()
    pg.display.set_caption("Project Phoenix")

    while True:
        update()
        Camera.Main.render()


def exit():
    pg.display.quit()
    pg.quit()
    sys.exit()


def update():

    global stateITRE
    global stateAxis

    # print(stateITRE, "//", stateAxis)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                exit()

            if event.key == pg.K_RETURN or event.key == pg.K_TAB or event.key == pg.K_q or event.key == pg.K_z:
                stateITRE = 0
                stateAxis = Vector3()
            if event.key == pg.K_t:
                stateITRE = 1
                stateAxis = Vector3()
            if event.key == pg.K_r:
                stateITRE = 2
                stateAxis = Vector3()
            if event.key == pg.K_e:
                stateITRE = 3
                stateAxis = Vector3(1, 1, 1)

            if event.key == pg.K_x:
                stateAxis.x = 1-stateAxis.x
            if event.key == pg.K_y:
                stateAxis.y = 1-stateAxis.y
            if event.key == pg.K_w:
                stateAxis.z = 1-stateAxis.z

    leftClick, middleClick, rightClick = pg.mouse.get_pressed()
    mouseDeltaPos = Vector(pg.mouse.get_rel()) * .005

    if middleClick:

        Transform3Master.Master.localPosRotScale3.rotate(Quaternion.eulerToQuaternion(
            Vector3(-mouseDeltaPos.y, mouseDeltaPos.x, 0)))
        return

    selectedEntity = Pyramid
    selectedPosRotScale = selectedEntity.transform.localPosRotScale3

    if stateITRE == 1:
        selectedPosRotScale.translate(stateAxis * mouseDeltaPos.x)
    elif stateITRE == 2:
        selectedPosRotScale.rotate(
            Quaternion.eulerToQuaternion(stateAxis*mouseDeltaPos.x))
    elif stateITRE == 3:
        selectedPosRotScale.scalate(Vector3.one + stateAxis * mouseDeltaPos.x)


main()
