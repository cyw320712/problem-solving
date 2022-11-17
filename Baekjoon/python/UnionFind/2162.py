from collections import defaultdict

n = int(input())
lines = []
parents = [i for i in range(n)]

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def crossProduct(p1:Point, p2:Point):
    return (p1.x*p2.y) - (p2.x*p1.y)

def direction(p1:Point, p2:Point, p3:Point):
    p31 = Point(p1.x - p3.x, p1.y - p3.y)
    p32 = Point(p2.x - p3.x, p2.y - p3.y)

    if crossProduct(p31, p32) > 0:
        return 1
    elif crossProduct(p31, p32) < 0:
        return -1
    
    return 0


def onSegment(a, b, c):
    if c.x >= min(a.x, b.x) and c.x <= max(a.x, b.x) \
        and c.y >= min(a.y, b.y) and c.y <= max(a.y, b.y):
        return True
    return False

def lineSegIntersect(p):
    d1 = direction(p[2], p[3], p[0])
    d2 = direction(p[2], p[3], p[1])
    d3 = direction(p[0], p[1], p[2])
    d4 = direction(p[0], p[1], p[3])
    
    if (d1*d2 < 0 and d3*d4 < 0): return True
    elif (d1 == 0 and onSegment(p[2], p[3], p[0])): return True
    elif (d2 == 0 and onSegment(p[2], p[3], p[1])): return True
    elif (d3 == 0 and onSegment(p[0], p[1], p[2])): return True
    elif (d4 == 0 and onSegment(p[0], p[1], p[3])): return True
    return False

def sameSomething(vector):
    for i in range(4):
        for j in range(4):
            if i == j: continue
            if vector[i].x == vector[j].x and vector[i].y == vector[j].y:
                return True
    return False

def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(parent, child):
    x = find(parent)
    y = find(child)

    parents[x] = y
    for i in range(n):
        if parents[i] == y:
            parents[i] = x
    return


for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    lines.append((p1, p2))

vector = [0] * 5
for i in range(n):
    cur = lines[i]
    vector[0] = cur[0]
    vector[1] = cur[1]
    
    for j in range(n):
        other = lines[j]
        vector[2] = other[0]
        vector[3] = other[1]

        if lineSegIntersect(vector):
            if find(j) != j:
                union(i, j)
            else:
                union(j, i)


candidates = set(parents)
values = defaultdict(int)

for i in candidates:
    values[i] = parents.count(i)

count = len(candidates)

print(count)
print(max(values.values()))
