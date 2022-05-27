from queue import PriorityQueue
import sys

(v, e) = map(int, input().split())
start = int(input())
INF = sys.maxsize
dist = [INF]*(v+1)

pq = PriorityQueue()
graph = [[] for _ in range(v+1)]

for _ in range(e):
  (x, y, w) = map(int, sys.stdin.readline().split())
  # (가중치, 도착지) 형태로 저장
  graph[x].append((w, y))

dist[start] = 0

# 주의: MIN HEAP이어야 됨.. (최단거리니까..)
pq.put((0, start))

while not pq.empty():
  # pq에서 하나씩 꺼내오기
  cur_w, cur_n = pq.get()

  # 만약 더 길면 pass
  if dist[cur_n] < cur_w:
    continue

  for w, next_node in graph[cur_n]:
    # 해당 노드와 연결된 노드들에 대해서 검색 후 넣기
    next_w = cur_w + w
    
    if next_w < dist[next_node]:
      dist[next_node] = next_w
      pq.put((next_w, next_node))

for i in range(1, v+1):
  if dist[i]==INF:
    print("INF")
  else:
    print(dist[i])