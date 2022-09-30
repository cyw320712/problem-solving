from collections import deque
import sys


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, sys.stdin.readline().split()))
    
    graph = [[] for _ in range(n+1)]
    indegree = [0] * (n+1)
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        indegree[y] += 1
    dest = int(input())

    queue = deque()

    result = [0] * (n+1)
    for i in range(1, n+1):
        if not indegree[i]:
            queue.append(i)
            result[i] = time[i]
    
    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            indegree[i] -= 1
            result[i] = max(result[cur]+time[i], result[i])
            if indegree[i] == 0:
                queue.append(i)

    print(result[dest])