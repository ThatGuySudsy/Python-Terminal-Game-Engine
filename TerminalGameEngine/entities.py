import render as r

class Rect:
    def __init__(self, name, texture, x, y, width, height, z = 0, enabled = True):
        self.name = name
        self.texture = str(texture)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.z = z
        self.enabled = enabled
        
        r.objects.append(self)
        r.objectMap[name] = self