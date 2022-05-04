from collections import deque
import sys


n, m = map(int, sys.stdin.readline().split())

board = [[0]*m for _ in range(n)]
for i in range(n):
  line = sys.stdin.readline()
  for j in range(m):
    board[i][j] = int(line[j])

dir_x = [-1, 0, 1, 0]
dir_y = [0, -1, 0, 1]

q = deque()
q.append((0, 0))
cost = deque()
cost.append(1)
visited = [[0] * m for _ in range(n)]

while q:
  cur = q.popleft()
  cur_x = cur[0]
  cur_y = cur[1]
  cur_c = cost.popleft()
  
  if cur_x == n-1 and cur_y == m-1:
    print(cur_c)
    break

  if visited[cur_x][cur_y]==1:
    continue
  visited[cur_x][cur_y] = 1

  for i in range(4):
    next_x = cur_x + dir_x[i]
    next_y = cur_y + dir_y[i]
    next_c = cur_c + 1
    if next_x >= 0 and next_x < n and next_y >= 0 and next_y < m:
      if visited[next_x][next_y]==0 and board[next_x][next_y]==1:
        q.append((next_x, next_y))
        cost.append(next_c)

