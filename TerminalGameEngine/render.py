from shutil import get_terminal_size as terminalSize
import os

objects = []
objectMap = {}

screenWidth = terminalSize().columns
screenHeight = terminalSize().lines

cameraX = 0
cameraY = 0

def render():
    os.system('cls' if os.name == 'nt' else 'clear')
    screen = [[" " for _ in range(screenWidth)] for _ in range(screenHeight)]
    for obj in sorted(objects, key=lambda obj: obj.z):
        if obj.enabled:
            if obj.type == "rect":
                for width in range(obj.width):
                    for height in range(obj.height):
                        if (screenWidth + cameraX >= obj.x + width >= cameraX) and (screenHeight+cameraY >= obj.y + height >= cameraY):
                            screen[obj.y+height-cameraY][obj.x+width-cameraX] = obj.texture
            elif obj.type == "text":
                obj.text = list(str(obj.text))
                if obj.isLocked:
                    for i in range (len(obj.text)):
                        if (cameraX+screenWidth >= obj.x+i >= cameraX) and (cameraY+screenHeight >= obj.y >= cameraY):
                            screen[obj.y-cameraY][obj.x+i-cameraX] = obj.text[i]
                    
    
    for y in range(screenHeight):
        toPrint = ""
        for x in range(screenWidth):
            toPrint += screen[y][x]
        print(toPrint)