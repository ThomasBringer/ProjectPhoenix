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


stateITRS = 0  # 0: idle, 1: translate, 2: rotate, 3: scalate
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

# def getMouse(event):
#     return 0 if event.type!=pg.MOUSEBUTTONDOWN else event.button


def update():

    global stateITRS
    global stateAxis

    # print(stateITRE, "//", stateAxis)

    selectedEntity = Pyramid
    selectedPosRotScale = selectedEntity.transform.localPosRotScale3

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            mouse = event.button
            if mouse == 1 or mouse == 3:
                stateITRS = 0
                stateAxis = Vector3()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                exit()

            if event.key == pg.K_RETURN or event.key == pg.K_TAB or event.key == pg.K_q or event.key == pg.K_z:
                stateITRS = 0
                stateAxis = Vector3()
            if event.key == pg.K_t:
                stateITRS = 1
                stateAxis = Vector3()
            if event.key == pg.K_r:
                stateITRS = 2
                stateAxis = Vector3()
            if event.key == pg.K_s:
                stateITRS = 3
                stateAxis = Vector3(1, 1, 1)

            if event.key == pg.K_x:
                stateAxis = Vector3.right
            if event.key == pg.K_y:
                stateAxis = Vector3.forward
            if event.key == pg.K_w:
                stateAxis = Vector3.up
            if event.key == pg.K_KP0:
                if stateITRS == 1:
                    selectedPosRotScale.position = Vector3()
                elif stateITRS == 2:
                    selectedPosRotScale.rotation = Quaternion()
                elif stateITRS == 3:
                    selectedPosRotScale.scale = Vector3(1, 1, 1)
                if stateITRS != 0:
                    stateITRS = 0
            if event.key == pg.K_KP5:
                Camera.Main.perspective = not Camera.Main.perspective

    leftClick, middleClick, rightClick = pg.mouse.get_pressed()
    mouseDeltaPos = Vector(pg.mouse.get_rel()) * .005

    if middleClick:

        Transform3Master.Master.localPosRotScale3.rotate(Quaternion.eulerToQuaternion(
            Vector3(-mouseDeltaPos.y, mouseDeltaPos.x, 0)))
        return

    if stateITRS == 1:
        selectedPosRotScale.translate(stateAxis * mouseDeltaPos.x)
    elif stateITRS == 2:
        selectedPosRotScale.rotate(
            Quaternion.eulerToQuaternion(stateAxis*mouseDeltaPos.x))
    elif stateITRS == 3:
        selectedPosRotScale.scalate(Vector3.one + stateAxis * mouseDeltaPos.x)


main()
