from collections import deque


n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
  [x, y] = list(map(int, input().split()))
  graph[x].append(y)
  graph[y].append(x)

count = 0
queue = deque([1])
visited = [0] * (n+1)
visited[1] = 1

while queue:
  cur = queue.popleft()

  for i in graph[cur]:
    if visited[i] == 0:
      count += 1
      queue.append(i)
      visited[i] = 1

print(count)