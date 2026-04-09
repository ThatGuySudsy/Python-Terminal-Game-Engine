import entities as e
import core as c
import render as r
import time as t

goomba = e.Rect("Goomba", "@", 50, 3, 2, 1, 0)
mario = e.Rect("Mario", "#", 60, 3, 2, 1, 1)


def Update():
    goomba.x -= 1
    mario.x -= 2

c.main_loop(Update)
