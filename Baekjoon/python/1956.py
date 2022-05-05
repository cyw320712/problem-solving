from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
board = [[int(1e12)]*n for _ in range(n)]

for i in range(m):
  x, y, w = map(int, sys.stdin.readline().split())
  x -=1
  y -=1
  board[x][y] = w

for i in range(n):
  board[i][i] = 0

for k in range(n):
  for i in range(n):
    for j in range(n):
      board[i][j] = min(board[i][j], board[i][k]+board[k][j])

min_len = int(1e12)
for i in range(n):
  for j in range(i+1, n):
    if board[i][j] != int(1e12) and board[j][i] != int(1e12):
      min_len = min(min_len, board[i][j] + board[j][i])

if min_len==int(1e12):
  print(-1)
else:
  print(min_len)