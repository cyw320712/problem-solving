import sys


n = int(input())
board = [[0] * n for _ in range(n)]

for i in range(n):
  line = list(map(int, sys.stdin.readline().split()))
  for j in range(n):
    board[i][j] = line[j]

for k in range(n):
  for i in range(n):
    for j in range(n):
      if board[i][k] and board[k][j]:
        board[i][j] = 1

for line in board:
  print(*line, sep=" ")