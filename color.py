from math import sqrt

class Color:
    def __init__(self, color: tuple[int, int, int]):
        self.core: bool = False
        self.color: tuple[int, int, int] = color
        self.count: int = 1
        self.clustered: bool = False
    def __str__(self):
        return f"Point: {self.position} - {self.color}"
    def setCore(self):
        self.core = True
    def setClustered(self):
        self.clustered = True
    def increaseCount(self):
        self.count += 1
    def getColor(self):
        return self.color
    def getDistance(self, p: 'Color') -> float:
        return sqrt((self.color[0] - p.color[0])**2 + (self.color[1] - p.color[1])**2 + (self.color[2] - p.color[2])**2)
    def isCore(self):
        return self.core
    def isClustered(self):
        return self.clustered