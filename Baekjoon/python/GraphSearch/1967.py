import sys
sys.setrecursionlimit(1000000000)


num = int(input())
graph = [[] for _ in range(num + 1)]
dist = [-1] * (num + 1)
dist[1] = 0

for _ in range(num-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append([child, weight])
    graph[child].append([parent, weight])

def dfs(x, wei):
    for node, weight in graph[x]:
        if dist[node] == -1:
            dist[node] = wei + weight
            dfs(node, weight + wei)

# 루트에서 가장 먼 노드 찾기
dfs(1, 0)

# 그 노드에서 가장 먼 노드 찾기 (그게 지름)
start = dist.index(max(dist))
dist = [-1] * (num + 1)
dist[start] = 0

dfs(start, 0)

print(max(dist))
