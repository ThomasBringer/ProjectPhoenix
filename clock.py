# Time management.

import pygame as pg

clock = pg.time.Clock()


def deltaTime(): return clock.get_time() / 1000


def tick(): return clock.tick()
