from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
board = [[0]*m for _ in range(n)]
cctv = []
rotate = [
  [],
  [[0], [1], [2], [3]],
  [[0,2], [1,3]],
  [[0, 1], [1, 2], [2, 3], [0, 3]],
  [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
  [[0, 1, 2, 3]],
]
global min_value
min_value = int(1e9)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cctv = []

for i in range(n):
  line = list(map(int, sys.stdin.readline().split()))
  for j in range(m):
    board[i][j] = line[j]
    if 0<line[j]<6:
      cctv.append([board[i][j], i, j])

def boundcheck(temp, cctvSight, x, y):
  for i in cctvSight:
    nx = x
    ny = y
    while True:
      nx += dx[i]
      ny += dy[i]
      if 0 > nx or nx >= n or  0 > ny or ny >= m:
        break
      if temp[nx][ny] == 6:
        break
      elif temp[nx][ny] == 0:
        temp[nx][ny] = 7

def dfs(cur, board):
  global min_value
  if cur == len(cctv):
    count = 0
    for i in range(n):
      count += board[i].count(0)
    min_value = min(min_value, count)
    return
  
  temp = [i[:] for i in board]
  cctv_num, x, y = cctv[cur]
  for sight in rotate[cctv_num]:
    boundcheck(temp, sight, x, y)
    dfs(cur+1, temp)
    temp = [i[:] for i in board]

dfs(0, board)
print(min_value)