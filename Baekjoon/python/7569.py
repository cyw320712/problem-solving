from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())

boards = []
zero_count = 0
q = deque()

for k in range(h):
  temp = []
  for i in range(n):
    temp.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
      if temp[i][j] == 0:
        zero_count += 1
      if temp[i][j] == 1:
        q.append((i, j, k))
  boards.append(temp)

zero = False

if zero_count == 0:
  print("0")
  zero = True
  
if not zero:
  dir_x = [-1, 1, 0, 0, 0, 0]
  dir_y = [0, 0, -1, 1, 0, 0]
  dir_z = [0, 0, 0, 0, -1, 1]
  
  while q:
    cur_x, cur_y, cur_z = q.popleft()
    cur_c = boards[cur_z][cur_x][cur_y]

    for i in range(6):
      next_x = cur_x + dir_x[i]
      next_y = cur_y + dir_y[i]
      next_z = cur_z + dir_z[i]
      if 0<=next_x<n and 0<=next_y <m and 0<=next_z < h and boards[next_z][next_x][next_y]==0:
        q.append((next_x, next_y, next_z))
        boards[next_z][next_x][next_y] = cur_c + 1
        zero_count -= 1

  if zero_count != 0:
    print("-1")
  else:
    max_value = 0
    for floor in boards:
      for line in floor:
        max_value = max(max(line), max_value)
    print(max_value-1)