from collections import deque
import sys

n = int(input())
boardA = [[0] * n for _ in range(n)]
boardB = [[0] * n for _ in range(n)]

def pb():
  print("A board")
  for line in boardA:
    print(line)
  print("B board")
  for line in boardB:
    print(line)

for i in range(n):
  line = input()
  for j in range(n):
    boardA[i][j] = line[j]
    if line[j] == 'G':
      boardB[i][j] = 'R'
    else:
      boardB[i][j] = line[j]

dir_x = [-1, 0, 1, 0]
dir_y = [0, -1, 0, 1]

def findnotvisited():
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        return i, j
  return -1, -1

def bfs(board, x, y):
  q = deque()
  q.append((x, y))
  while q:
    cur = q.popleft()
    cur_x = cur[0]
    cur_y = cur[1]
    cur_c = board[cur_x][cur_y]

    if visited[cur_x][cur_y]:
      continue
    visited[cur_x][cur_y] = 1

    for i in range(4):
      next_x = cur_x + dir_x[i]
      next_y = cur_y + dir_y[i]
      if next_x >= 0 and next_x < n and next_y >= 0 and next_y < n:
        if not visited[next_x][next_y] and board[next_x][next_y]==cur_c:
          q.append((next_x, next_y))

visited= [[0] * n for _ in range(n)]
countA = 0
x, y = findnotvisited()
while x != -1:
  countA += 1
  bfs(boardA, x, y)
  x, y = findnotvisited()
visited= [[0] * n for _ in range(n)]
countB = 0
x, y = findnotvisited()
while x != -1:
  countB += 1
  bfs(boardB, x, y)
  x, y = findnotvisited()

print(countA, countB)