from collections import deque
import sys


n, m = map(int, sys.stdin.readline().split())

q = deque()
q.append((n, 0))
visited = [0] * 200001
cost = 0
while(q):
  cur, cost = q.popleft()
  
  if cur == m:
    break

  for i in range(3):
    nc = cost + 1
    if i == 0:
      nx = cur - 1
    elif i == 1:
      nx = cur + 1
    else:
      nx = cur * 2
    
    if 0 <= nx < 100001:
      if not visited[nx]:
        q.append((nx,nc))
        visited[nx] = 1

print(cost)