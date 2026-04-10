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
        
        self.type = "rect"
        
        r.objects.append(self)
        r.objectMap[name] = self
        
class Text:
    def __init__(self, name, text, x, y, isLocked = True, z = 0, enabled = True):
        self.name = name
        self.text = list(str(text))
        self.x = x
        self.y = y
        self.isLocked = isLocked
        self.z = z
        self.enabled = enabled
        
        self.type = "text"
        
        r.objects.append(self)
        r.objectMap[name] = self