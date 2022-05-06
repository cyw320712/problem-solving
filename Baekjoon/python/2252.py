from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
inDegree = [ 0 for _ in range(32000)]
graph = [[] for _ in range(32000)]
q = deque()

for _ in range(m):
  start, end = map(int, sys.stdin.readline().split())
  start -= 1
  end -= 1
  inDegree[end] += 1
  graph[start].append(end)

for i in range(n):
  if not inDegree[i]:
    q.append(i)

while q:
  cur = q.popleft()
  for j in graph[cur]:
    inDegree[j] -= 1
    if inDegree[j] == 0:
      q.append(j)
  print(cur+1, end=" ")
