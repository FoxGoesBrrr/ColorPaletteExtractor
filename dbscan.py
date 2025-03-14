from color import Color
from collections import defaultdict, deque

class DBScan:
    def __init__(self, colors: list[Color], epsilon: float, minPts: int):
        self.colors = colors
        self.epsilon = epsilon
        self.minPts = minPts
        self.clusters = []
        self.outliers = []
        self.neighbors_map = defaultdict(list)
        
    def run(self):
        self._precompute_neighbors()
        
        for i, c in enumerate(self.colors):
            if len(self.neighbors_map[i]) >= self.minPts:
                c.setCore()
        
        for i, c in enumerate(self.colors):
            if not c.isClustered() and c.isCore():
                cluster = self._form_cluster(i)
                self.clusters.append(cluster)
    
    def _precompute_neighbors(self):
        n = len(self.colors)
        for i in range(n):
            for j in range(i + 1, n):  
                if self.colors[i].getDistance(self.colors[j]) <= self.epsilon:
                    self.neighbors_map[i].append(j)
                    self.neighbors_map[j].append(i)
    
    def _form_cluster(self, point_idx: int) -> list[Color]:
        cluster = []
        queue = deque([point_idx])
        processed = set()
        
        while queue:
            idx = queue.popleft()  
            if idx in processed:
                continue
                
            processed.add(idx)
            point = self.colors[idx]
            
            if not point.isClustered():
                point.setClustered()
                cluster.append(point)
                
                if point.isCore():
                    for neighbor_idx in self.neighbors_map[idx]:
                        if neighbor_idx not in processed:
                            queue.append(neighbor_idx)
                            
        return cluster
    
    def getClusters(self) -> list[list[Color]]:
        return self.clusters
    
    def getOutliers(self) -> list[Color]:
        if not self.outliers:
            self.outliers = [c for c in self.colors if not c.isClustered()]
        return self.outliers