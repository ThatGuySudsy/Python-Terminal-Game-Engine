import entities as e
import core as c
import render as r

# e.Rect("Name", "Texture Character", x, y, width, height, z (optional, default is 0), enabled (optional, default is True))
# e.Text("Name", "Text", x, y, isLocked (optional, default is True), z (optional, default is 0), enabled (optional, default is True))

goomba = e.Rect("Goomba", "@", 50, 3, 2, 1, 0)
mario = e.Rect("Mario", "#", 60, 3, 2, 1, 1)
label = e.Text("Label", mario.x, 5, 10)


def Update():
    goomba.x -= 1
    mario.x -= 2
    label.text = mario.x

c.main_loop(Update)