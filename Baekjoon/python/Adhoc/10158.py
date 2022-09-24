w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 개미가 이동한 거리 - 왕복한 거리
a = (p + t) // w
b = (q + t) // h

if a % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if b % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)