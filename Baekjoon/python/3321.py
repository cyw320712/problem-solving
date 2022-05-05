import sys

n, m = map(int, sys.stdin.readline().split())
board = [[0]*m for _ in range(n)]
for i in range(n):
  line = sys.stdin.readline()
  for j in range(m):
    board[i][j] = int(line[j])


for i in range(1, n):
  for j in range(m):
    if board[i][j] == 1:
      board[i][j] = board[i-1][j] + 1

max_size = 0
for i in range(n):
  line = board[i]
  line.sort(reverse=True)
  for j in range(m):
    size = (j+1) * line[j]
    max_size = max(max_size, size)

print(max_size)


