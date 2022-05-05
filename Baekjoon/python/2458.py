import sys

n, m = map(int, sys.stdin.readline().split())
board = [[0] * n for _ in range(n)]

for i in range(m):
  x, y = map(int, sys.stdin.readline().split())
  x-=1
  y-=1
  board[x][y] = 1
  board[y][x] = -1

for k in range(n):
  for i in range(n):
    for j in range(n):
      if board[i][k]==1 and board[k][j]==1:
        board[i][j] = 1
        board[j][i] = -1
      elif board[i][k]==-1 and board[k][j]==-1:
        board[i][j] = -1
        board[j][i] = 1

result = 0
for i in range(n):
  flag = True
  for j in range(n):
    if i==j:
      continue
    if board[i][j] == 0:
      flag = False
  if flag:
    result += 1

print(result)
