from collections import deque
import sys

m, n = map(int, sys.stdin.readline().split())

board = [[0]*m for _ in range(n)]
zero_count = 0
q = deque()

for i in range(n):
  temp = list(map(int, sys.stdin.readline().split()))
  for j in range(m):
    if temp[j] == 0:
      zero_count += 1
    if temp[j] == 1:
      q.append((i, j))
    board[i][j] = temp[j]

zero = False

if zero_count == 0:
  print("0")
  zero = True
  
if not zero:
  dir_x = [-1, 1, 0, 0]
  dir_y = [0, 0, -1, 1]
  
  while q:
    cur_x, cur_y = q.popleft()
    cur_c = board[cur_x][cur_y]

    for i in range(4):
      next_x = cur_x + dir_x[i]
      next_y = cur_y + dir_y[i]
      if 0<=next_x<n and 0<=next_y <m and board[next_x][next_y]==0:
        q.append((next_x, next_y))
        board[next_x][next_y] = cur_c + 1
        zero_count -= 1

  if zero_count != 0:
    print("-1")
  else:
    max_value = 0
    for line in board:
      max_value = max(max(line), max_value)
    print(max_value-1)