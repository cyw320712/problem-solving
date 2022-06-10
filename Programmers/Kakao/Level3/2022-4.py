from collections import deque


def solution(n, paths, gates, summits):
  answer = []
  graph = [[] for _ in range(n)]
  result = deque()
  for path in paths:
    start, end, w = path
    start -= 1
    end -= 1
    graph[start].append([end, w])
    graph[end].append([start, w])
  # print(graph)
  for gate in gates:
    q = deque()
    q.append((gate-1, 0))
    # intensity = 0
    visited = [0]*n
    visited[gate-1] = 1
    while q:
      # print(q)
      cur, intensity = q.pop()
      visited[cur] = 1
      
      for i in range(len(graph[cur])):
        npos = graph[cur][i][0]

        if npos+1 in gates:
          continue
        if not visited[npos]:
          weight = graph[cur][i][1]
          nintensity = max(intensity, weight)
          
          if npos+1 in summits:
            print(f"{gate}: {npos}, {nintensity}")
            result.append((npos+1, nintensity))
            continue
          
          q.append((npos, nintensity))
  result = list(result)
  print(result)
  result = sorted(result, key=lambda x:(x[1], x[0]))
  answer = list(result[0])
  return answer

print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))