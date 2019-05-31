import json
import sys

from PIL import Image


depth = Image.open(sys.argv[1])
done = Image.new('1', depth.size)
obstacles = []

def largest_square(x, y):
    z = depth.getpixel((x, y))
    size = 1
    while True:
        size += 1
        for j in range(size):
            for i in range(size):
                if (x + i >= depth.size[0] or y + j >= depth.size[1]
                        #or done.getpixel((x + i, y + j))
                        or z != depth.getpixel((x + i, y + j))):
                    return size - 1

for y in range(depth.size[1]):
    for x in range(depth.size[0]):
        z = depth.getpixel((x, y))
        if z >= 20 or done.getpixel((x, y)):
            continue
        sq = largest_square(x, y)
        for j in range(sq):
            for i in range(sq):
                done.putpixel((x + i, y + j), 1)
        obstacle = (x - 1, y - 1, z - 1, x + sq + 1, y + sq + 2, z + 2)
        obstacles.append(obstacle)

print(len(obstacles), file=sys.stderr)
print(json.dumps(obstacles))
