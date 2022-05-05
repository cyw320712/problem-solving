import sys

n, m = map(int, sys.stdin.readline().split())

result = [0]*10
visited = [0]*10

def backtrack(k):
  if k == m:
    for i in range(m):
      print(result[i], end=" ")
    print("")
    return
  for i in range (1, n+1):
    if not visited[i]:
      result[k] = i
      visited[i] = 1
      backtrack(k+1)
      visited[i] = 0

backtrack(0)