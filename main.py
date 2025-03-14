from PIL import Image

from color import Color
from dbscan import DBScan

image = Image.open("test2.jpg")
x, y = image.size

print(f"Image size: {x}x{y}")
colors: list[Color] = []
for i in range(x):
    for j in range(y):
        r, g, b = image.getpixel((i, j))
        pixel = (r, g, b)
        found = False
        for c in colors:
            if c.getColor() == pixel:
                c.increaseCount()
                found = True
                break
        if not found:
            colors.append(Color(pixel))
print("Scanned all the colors in the image.")

dbscan = DBScan(colors, 20, 6)
print("Running DBScan...")
dbscan.run()
clusters = dbscan.getClusters()
outliers = dbscan.getOutliers()
print(f"Number of clusters: {len(clusters)}")
print(f"Outliers: {len(outliers)}")
for i, c in enumerate(clusters):
    print(f"Cluster {i}: {len(c)}")
for i, o in enumerate(outliers):
    print(f"Outlier {i}: {o.getColor()}")
