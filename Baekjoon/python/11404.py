import sys

n = int(input())
m = int(input())
floyd = [[int(1e12)]*n for _ in range(n)]

for _ in range(m):
  x, y, w = map(int, sys.stdin.readline().split())
  x -=1
  y -=1
  floyd[x][y] = min(floyd[x][y], w)

def pa():
  for line in floyd:
    for item in line:
      if item == int(1e12):
        print(0, end=" ")
      else:
        print(item, end=" ")
    print()

for stand in range(0, n):
  for i in range(0, n):
    for j in range(0, n):
      if i==j:
        floyd[i][j] = 0
        continue
      if floyd[i][stand] != 0 and floyd[stand][j] != 0:
          floyd[i][j] = min(floyd[i][j], floyd[i][stand] + floyd[stand][j])

pa()