# Main script. Main update & input management.
# Commands:
# Mouse buttons or alt to orbit the view.
# Mouse wheel to zoom in and out.
# P to start and pause the simulation.
# Numpad 5 to switch between perspective and orthographic.

import pygame as pg
import sys
import numpy as np

from camera import *
from color import *
from simulations import *
from mesh import *

from transform3 import *
from unit import *
from space import *
from clock import *
from physics import *

# A state system for controlling objects.  0: idle, 1: translate, 2: rotate, 3: scalate.
stateITRS = 0

stateAxis = Vector3()


def main():
    pg.init()
    pg.display.set_mode((1440, 1080), pg.FULLSCREEN, 0)
    pg.display.set_caption("Project Phoenix")

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
        behaviorUpdate()
    inputUpdate()
    Camera.Main.render()


def behaviorUpdate():
    for updatableUnit in UpdatableUnits:
        updatableUnit.update()


selectedPosRotScale = selectedEntity.transform.localPosRotScale3


def inputUpdate():

    global stateITRS
    global stateAxis
    global paused

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
            if event.key == pg.K_o:
                if paused:
                    behaviorUpdate()
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

    leftClick, middleClick, rightClick = pg.mouse.get_pressed()
    mouseDeltaPos = Vector2(pg.mouse.get_rel()) * .005

    if leftClick or middleClick or rightClick or alt:

        Transform3Master.Master.localPosRotScale3.rotate(Quaternion.eulerToQuaternion(
            Vector3.left * mouseDeltaPos.y * (0 if shift else 1) - Transform3Master.Master.localPosRotScale3.rotation.localUp * mouseDeltaPos.x * (0 if ctrl else 1)))
        return

    if stateITRS == 1:
        selectedPosRotScale.translate(stateAxis * mouseDeltaPos.x)
    elif stateITRS == 2:
        selectedPosRotScale.rotate(
            Quaternion.eulerToQuaternion(stateAxis * mouseDeltaPos.x))
    elif stateITRS == 3:
        selectedPosRotScale.scalate(Vector3.one + stateAxis * mouseDeltaPos.x)


main()
