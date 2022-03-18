from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())

graph = {i:[] for i in range(1, n+1)}

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(n, start):
    kevin = [0] * (n+1)
    visited = [start]
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if i not in visited:
                kevin[i] = kevin[cur] + 1
                queue.append(i)
                visited.append(i)
    return sum(kevin)

result = []
for i in range(1, n+1):
    result.append(bfs(n, i))

# print(result)
print(result.index(min(result)) + 1)
