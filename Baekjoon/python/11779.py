from collections import deque
import sys
from queue import PriorityQueue

e = int(input())
v = int(input())
INF = 1e9 + 10
dist = [INF] * (e+1)
graph = [[] for _ in range(e+1)]
pq = PriorityQueue()

# pre 배열은 이전 
pre = [-1] * (e+1)

for _ in range(v):
  x, y, w = map(int, sys.stdin.readline().split())
  graph[x].append((w, y))

start, end = map(int, input().split())
dist[start] = 0
pq.put((0, start))

# 다익스트라 시작
while not pq.empty():
  cur_cost, cur_node = pq.get()

  # 모든 경로 체크시 항상 시간초과!!
  # 지금 거리보다 더 큰 경우 continue!
  if cur_cost > dist[cur_node]:
    continue

  for cost, next_node in graph[cur_node]:
    next_cost = cur_cost + cost
    if next_cost < dist[next_node]:
      dist[next_node] = next_cost
      pq.put((next_cost, next_node))
      # 갱신될 때 pre 배열도 갱신
      pre[next_node] = cur_node


# 해당 최단 경로 찾기
route = deque([end])
prev = end
while pre[prev] != -1:
  route.appendleft(pre[prev])
  prev = pre[prev]

print(dist[end])
print(len(route))
print(' '.join(map(str, route)))