import render as r

class Rect:
    def __init__(self, name, x, y, width, height):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        r.objects.append(self)
        r.objectMap[name] = self