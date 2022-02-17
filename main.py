import pygame as pg
import sys
import numpy as np

from camera import *
from color import *
from simulations import *
from matrix2x2 import *
from mesh import *
# from segment2 import *
# from segment3 import *
from transform3 import *
from unit import *
from space import *
from clock import *
from physics import *

stateITRS = 0  # 0: idle, 1: translate, 2: rotate, 3: scalate
stateAxis = Vector3()


def main():
    pg.init()
    pg.display.set_caption("Project Phoenix")

    # print(len(Meshes))

    # print(Track01.units[0])
    # print(Track01.units[0].points)

    # print(Track01.units[0].segs)

    # print("right", Cart.transform.localPosRotScale3.rotation.localRight, "forward",
    #       Cart.transform.localPosRotScale3.rotation.localForward, "up", Cart.transform.localPosRotScale3.rotation.localUp)

    # Cart.transform.localPosRotScale3.rotation.localForward = Vector3.up
    while True:
        mainUpdate()


def exit():
    pg.display.quit()
    pg.quit()
    sys.exit()


paused = True


def mainUpdate():
    tick()
    if not paused:
        for updatableUnit in UpdatableUnits:
            updatableUnit.update()
    inputUpdate()
    Camera.Main.render()


selectedPosRotScale = selectedEntity.transform.localPosRotScale3


def inputUpdate():

    global stateITRS
    global stateAxis
    global paused

    # print(stateITRE, "//p", stateAxis)

    pressed = pg.key.get_pressed()
    alt = pressed[pg.K_LALT] or pressed[pg.K_RALT]
    shift = pressed[pg.K_RSHIFT] or pressed[pg.K_LSHIFT]
    ctrl = pressed[pg.K_LCTRL] or pressed[pg.K_RCTRL]

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse = event.button
            if mouse == 1 or mouse == 3:
                stateITRS = 0
                stateAxis = Vector3()
            elif mouse == 4 or mouse == 5:
                scroll = 1 if mouse == 4 else -1 if mouse == 5 else 0
                # pressed = pg.key.get_pressed()
                # shift = pressed[pg.K_RSHIFT] or pressed[pg.K_LSHIFT]
                if shift:
                    if Camera.Main.perspective:
                        Camera.Main.persScaler -= scroll * .025
                else:
                    Camera.Main.orthoSize *= 1 + scroll * .1

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                exit()
            if event.key == pg.K_p:
                paused = not paused
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
                stateAxis = Vector3(1, 1, 1) if stateAxis != Vector3(
                    1, 1, 1) else Vector3(0, 0, 0)

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

            if event.key == pg.K_KP1:
                print(Transform3Master.Master.localPosRotScale3.rotation)

            if event.key == pg.K_KP2:
                Transform3Master.Master.localPosRotScale3.rotation = Quaternion(
                    0.92388, Vector3(0.382683, 0, 0))

            # if event.key == pg.K_KP1:
            #     Transform3Master.Master.localPosRotScale3.rotation.face(
            #         Vector3(0, 1, 0))
            # if event.key == pg.K_KP3:
            #     Transform3Master.Master.localPosRotScale3.rotation.face(
            #         Vector3(-1, 0, 0))
            # if event.key == pg.K_KP7:
            #     Transform3Master.Master.localPosRotScale3.rotation.face(
            #         Vector3(0, -1, 0))
            # if event.key == pg.K_KP9:
            #     Transform3Master.Master.localPosRotScale3.rotation.face(
            #         Vector3(1, 0, 0))

            # if event.key == pg.K_KP8:
            #     Transform3Master.Master.localPosRotScale3.rotation.localUp = -Vector3.forward
            # if event.key == pg.K_KP1:
            #     Transform3Master.Master.localPosRotScale3.rotation = Quaternion(
            #         0.707107, Vector3(0, 0, 0.707107))
            # if event.key == pg.K_KP3:
            #     Transform3Master.Master.localPosRotScale3.rotation.localForward = -Vector3.forward
            # if event.key == pg.K_KP7:
            #     Transform3Master.Master.localPosRotScale3.rotation.localUp = -Vector3.forward

    leftClick, middleClick, rightClick = pg.mouse.get_pressed()
    mouseDeltaPos = Vector2(pg.mouse.get_rel()) * .005

    if middleClick or alt:

        Transform3Master.Master.localPosRotScale3.rotate(Quaternion.eulerToQuaternion(
            Vector3.left * mouseDeltaPos.y * (0 if shift else 1) - Transform3Master.Master.localPosRotScale3.rotation.localUp * mouseDeltaPos.x * (0 if ctrl else 1)))

        # print(Transform3Master.Master.localPosRotScale3.rotation.localUp)

        # Transform3Master.Master.localPosRotScale3.rotate(Quaternion.eulerToQuaternion(
        #     Vector3.left * mouseDeltaPos.y * (0 if shift else 1) + Vector3.forward * mouseDeltaPos.x * (0 if ctrl else 1)))

#         Transform3Master.Master.localPosRotScale3.rotate(Quaternion.eulerToQuaternion(Vector3.left*mouseDeltaPos.y))
# Transform3Master.Master.localPosRotScale3.rotate(Quaternion.eulerToQuaternion(
#             Vector3(-mouseDeltaPos.y * (0 if shift else 1), mouseDeltaPos.x * (0 if ctrl else 1), 0)))

        return

    if stateITRS == 1:
        selectedPosRotScale.translate(stateAxis * mouseDeltaPos.x)
    elif stateITRS == 2:
        selectedPosRotScale.rotate(
            Quaternion.eulerToQuaternion(stateAxis * mouseDeltaPos.x))
    elif stateITRS == 3:
        selectedPosRotScale.scalate(Vector3.one + stateAxis * mouseDeltaPos.x)


main()
