class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

p1 = Point(x1, y1)
p2 = Point(x2, y2)
p3 = Point(x3, y3)
p4 = Point(x4, y4)

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

if lineSegIntersect([p1, p2, p3, p4]):
    print(1)
else:
    print(0)