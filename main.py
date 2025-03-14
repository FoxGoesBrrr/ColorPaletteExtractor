from PIL import Image

from color import Color
from dbscan import DBScan

image = Image.open("test.png")
x, y = image.size

print(f"Image size: {x}x{y}")

color_dict = {}

for i in range(x):
    for j in range(y):
        pixel = image.getpixel((i, j))
        if pixel in color_dict:
            color_dict[pixel].increaseCount()
        else:
            color_dict[pixel] = Color(pixel)

colors = list(color_dict.values())
print(f"Scanned all the colors in the image. Found {len(colors)} unique colors.")

dbscan = DBScan(colors, 10, 3)
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

for cluster in clusters:
    r_sum, g_sum, b_sum = 0, 0, 0
    for color in cluster:
        r_sum += color.color[0]
        g_sum += color.color[1]
        b_sum += color.color[2]
    r_median = r_sum // len(cluster)
    g_median = g_sum // len(cluster)
    b_median = b_sum // len(cluster)
    print(f"Cluster median color: rgb({r_median}, {g_median}, {b_median})")

