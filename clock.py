import pygame as pg

clock = pg.time.Clock()

deltaTime = lambda: clock.get_time() / 1000

tick = lambda: clock.tick()
