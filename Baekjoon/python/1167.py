from collections import deque
import sys


n = int(input())
tree = [[] for _ in range(n)]

for _ in range(n):
  line = list(map(int, sys.stdin.readline().split()))
  for j in range(1, len(line)-1, 2):
    v, w = line[j]-1, line[j+1]
    tree[line[0]-1].append([v, w])

s = deque()
radius = 0
index = 0
visited = [0] *n

s.append((0, 0))
visited[0] = 1
while s:
  cur, cost = s.pop()
  
  if cost > radius:
    index = cur
    radius = cost

  for v, w in tree[cur]:
    if w != 0:
      if not visited[v]:
        visited[v] = 1
        next_cost = w + cost
        s.append((v, next_cost))

s.append((index, 0))
for j in range(n):
  visited[j] = 0
visited[index] = 1
while s:
  cur, cost = s.pop()
  
  if cost > radius:
    index = cur
    radius = cost

  for v, w in tree[cur]:
    if w != 0:
      if not visited[v]:
        visited[v] = 1
        next_cost = w + cost
        s.append((v, next_cost))
          
print(radius)
