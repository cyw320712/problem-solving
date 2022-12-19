n = int(input())

points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append([x, y])
points.append(points[0])

space = 0
for i in range(n):
    cx, cy = points[i]
    nx, ny = points[i+1]
    space += (cx * ny) - (nx * cy)

print(round(abs(space)/2, 1))