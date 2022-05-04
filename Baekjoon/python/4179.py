import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rsplit())

board = [[0] * k for _ in range(n)]
visited = [[0] * k for _ in range(n)]
arrival = [[0] * k for _ in range(n)]
fire = [[100000001] * k for _ in range(n)]
q = deque()

start = []
for i in range(n):
  line = sys.stdin.readline()
  for j in range(k):
    if line[j]=="J":
      arrival[i][j] = 1
      start = [i, j]
    elif line[j] == 'F':
      q.append([i, j])
      fire[i][j] = 1
      visited[i][j] = 1
    board[i][j] = line[j]

dir_x = [1, 0, -1, 0]
dir_y = [0, 1, 0, -1]

# 불 BFS 먼저
while q:
  cur = q.popleft()
  cur_x = cur[0]
  cur_y = cur[1]

  for i in range(4):
    next_x = cur[0]+dir_x[i]
    next_y = cur[1]+dir_y[i]
    next_cost = fire[cur_x][cur_y] + 1
    if next_x >= 0 and next_x < n and next_y >= 0 and next_y < k:
      if visited[next_x][next_y] == 0:
        if board[next_x][next_y] != "#":
          q.append([next_x, next_y])
          fire[next_x][next_y] = next_cost
          visited[next_x][next_y] = 1

visited = [[0] * k for _ in range(n)]
flag = False
q.append(start)

def pa():
  print("===fire===")
  for line in fire:
    print(line)
  print("===Jinsu===")
  for line in arrival:
    print(line)

while q:
  cur = q.popleft()
  cur_x = cur[0]
  cur_y = cur[1]
  cur_c = arrival[cur_x][cur_y]

  if visited[cur[0]][cur[1]] == 1:
    continue
  visited[cur[0]][cur[1]] = 1
  board[cur_x][cur_y] = "J"
  if cur_x == 0 or cur_x == n-1 or cur_y == 0 or cur_y == k-1:
    flag = True
    break

  for i in range(4):
    next_x = cur[0]+dir_x[i]
    next_y = cur[1]+dir_y[i]
    next_c = cur_c + 1
    if next_x >= 0 and next_x < n and next_y >= 0 and next_y < k:
      if visited[next_x][next_y] == 0:
        if board[next_x][next_y] != "#" and next_c < fire[next_x][next_y]:
          q.append([next_x, next_y])
          arrival[next_x][next_y] = next_c

if flag:
  print(arrival[cur_x][cur_y])
else:
  print("IMPOSSIBLE")