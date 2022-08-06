from collections import deque
import sys


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
connected = 0

for _ in range(m):
  x, y = map(int, sys.stdin.readline().split())
  graph[x].append(y)
  graph[y].append(x)

for i in range(1, n+1):
  if visited[i] == 1:
    continue

  queue = deque()
  queue.append(i)
  visited[i] = 1
  connected += 1

  while queue:
    cur = queue.popleft()

    for i in graph[cur]:
      if visited[i] == 0:
        queue.append(i)
        visited[i] = 1

print(connected)
