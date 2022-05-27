from queue import PriorityQueue
import sys


n = int(input())
m = int(input())
INF = 1e9 + 10
pq = PriorityQueue()
dist = [INF] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
  x, y, w = map(int, sys.stdin.readline().split())
  graph[x].append((w, y))
start, end = map(int, input().split())

dist[start] = 0
pq.put((0, start))

while not pq.empty():
  cur_cost, cur_node = pq.get()

  if cur_cost > dist[cur_node]:
    continue

  for cost, next_node in graph[cur_node]:
    next_cost = cur_cost + cost
    if next_cost < dist[next_node]:
      dist[next_node] = next_cost
      pq.put((next_cost, next_node))

print(dist[end])