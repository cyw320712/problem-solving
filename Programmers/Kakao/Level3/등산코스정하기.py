from collections import defaultdict
from queue import PriorityQueue


def solution(n, paths, gates, summits):
  answer = []

  summits.sort()
  summits = set(summits)
  INF = 10000001
  visited = [INF] * (n+1)
  graph = defaultdict(list)
  pq = PriorityQueue()

  for x, y, w in paths:
    graph[x].append((w, y))
    graph[y].append((w, x))

  for gate in gates:
    pq.put((0, gate))
    visited[gate] = 0
  
  while not pq.empty():
    cur_cost, cur_node = pq.get()

    if cur_node in summits or cur_cost > visited[cur_node]:
      continue

    for cost, next_node in graph[cur_node]:

      next_cost = max(cost, cur_cost)

      if next_cost < visited[next_node]:
        visited[next_node] = next_cost
        pq.put((next_cost, next_node))
  
  answer = [0, INF]
  for summit in summits:
    if visited[summit] < answer[1]:
      answer[0] = summit
      answer[1] = visited[summit]

  return answer