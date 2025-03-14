from PIL import Image

from color import Color

image = Image.open("test.png")
x, y = image.size

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

