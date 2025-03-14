from PIL import Image
from math import sqrt

image = Image.open("test.png")
x, y = image.size

class Point:
    def __init__(self, color: tuple[int, int, int], position: tuple[int, int]):
        self.core: bool = False
        self.color: tuple[int, int, int] = color
        self.position: tuple[int, int] = position
    def __str__(self):
        return f"Point: {self.position} - {self.color}"
    def setCore(self):
        self.core = True
    def getColor(self):
        return self.color

total_colors = []
for i in range(x):
    colors = []
    for j in range(y):
        r, g, b = image.getpixel((i, j))
        colors.append(Point((r, g, b), (i, j)))
    total_colors.append(colors)

def getDistance(p1: Point, p2: Point) -> float:
    return sqrt((p1.color[0] - p2.color[0])**2 + (p1.color[1] - p2.color[1])**2 + (p1.color[2] - p2.color[2])**2)

