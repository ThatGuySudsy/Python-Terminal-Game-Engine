import render as r

class Rect:
    def __init__(self, name, texture, x, y, width, height, z = 0):
        self.name = name
        self.texture = str(texture)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.z = z
        r.objects.append(self)
        r.objectMap[name] = self