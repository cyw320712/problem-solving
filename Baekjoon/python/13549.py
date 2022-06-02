from queue import PriorityQueue


start, end = map(int, input().split())
INF = (1e12)
dist = [INF]*(100001)
graph = [[] for _ in range(100001)]

for i in range(0, 100001):
  if i-1 >= 0:
    graph[i].append((1, i-1))
  if i+1 <= 100000:
    graph[i].append((1, i+1))
  if 0 < i*2 <= 100000:
    graph[i].append((0, i*2))

dist[start] = 0
pq = PriorityQueue()
pq.put((0, start))
while not pq.empty():
  cur_cost, cur_node = pq.get()
  # print(f"===={cur_node}====")

  if cur_cost > dist[cur_node]:
    continue

  for cost, next_node in graph[cur_node]:
    next_cost = cost + cur_cost
    if next_cost < dist[next_node]:
      dist[next_node] = next_cost
      pq.put((next_cost, next_node))
      # print(f"{cur_node} put => {next_node}: {next_cost}")

# print(dist)
print(dist[end])