from math import sqrt

class Color:
    __slots__ = ('core', 'color', 'count', 'clustered')
    
    def __init__(self, color: tuple[int, int, int]):
        self.core: bool = False
        self.color: tuple[int, int, int] = color
        self.count: int = 1
        self.clustered: bool = False
    
    def __str__(self):
        return f"Color: {self.color} (count: {self.count})"
    
    def setCore(self):
        self.core = True
        
    def setClustered(self):
        self.clustered = True
        
    def increaseCount(self):
        self.count += 1
        
    def getColor(self):
        return self.color
    
    def getDistance(self, p: 'Color') -> float:
        r_diff = self.color[0] - p.color[0]
        g_diff = self.color[1] - p.color[1]
        b_diff = self.color[2] - p.color[2]
        return sqrt(r_diff*r_diff + g_diff*g_diff + b_diff*b_diff)
    
    def isCore(self):
        return self.core
        
    def isClustered(self):
        return self.clustered