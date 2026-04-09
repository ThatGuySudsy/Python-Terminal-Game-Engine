import entities as e
import render as r
import time as t

goomba = e.Rect("Goomba", "@", 50, 3, 2, 1)
mario = e.Rect("Mario", "#", 60, 3, 2, 0)

while True:
    r.render()
    goomba.x -= 1
    mario.x -= 2
    t.sleep(0.1)