from color import Color

class DBScan:
    def __init__(self, colors: list[Color], epsilon: float, minPts: int):
        self.colors: list[Color] = colors
        self.epsilon: float = epsilon
        self.minPts: int = minPts
        self.clusters: list[list[Color]] = []
        self.outliers: list[Color] = []
    def run(self):
        for c in self.colors:
            if self.__countNeighbors(c) >= self.minPts:
                c.setCore()
        for c in self.colors:
            if not c.isClustered() and c.isCore():
                cluster = self.__formClusters(c)
                self.clusters.append(cluster)
    def __countNeighbors(self, p: Color) -> int:
        count: int = 0
        for c in self.colors:
            if p.getColor == c.getColor:
                continue
            if p.getDistance(c) <= self.epsilon:
                count += 1
        return count
    def __formClusters(self, p: Color) -> list[Color]:
        cluster: list[Color] = []
        for c in self.colors:
            if c.isClustered():
                continue
            if p.getDistance(c) <= self.epsilon:
                c.setClustered()
                cluster.append(c)
        return cluster
    def getClusters(self) -> list[list[Color]]:
        return self.clusters
    def getOutliers(self) -> list[Color]:
        if not self.outliers:
            for c in self.colors:
                if not c.isClustered():
                    self.outliers.append(c)
        return self.outliers