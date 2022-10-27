from collections import deque


n = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
q = deque()

for _ in range(n-1):
    parent, child = map(int, input().split())
    graph[parent].append(child)
    graph[child].append(parent)

q.append(1)
visited[1] = 1

while q:
    cur = q.popleft()

    for child in graph[cur]:
        if visited[child] == 0:
            q.append(child)
            visited[child] = cur

for i in range(2, n+1):
    print(visited[i])