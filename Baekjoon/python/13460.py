from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
board = [[0] * m for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
rx, ry, bx, by = 0, 0, 0, 0
for i in range(n):
  line = sys.stdin.readline()
  for j in range(m):
    board[i][j] = line[j]
    if line[j] == 'R':
      rx, ry = i, j
    elif line[j] == 'B':
      bx, by = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
q = deque()
q.append((rx, ry, bx, by, 1))
visited[rx][ry][bx][by] = True

def move(x, y, dx, dy):
  cnt = 0
  while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
    x += dx
    y += dy
    cnt += 1
  return x, y, cnt
success = False
while q:
  if success:
    break
  rx, ry, bx, by, cost = q.popleft()
  if cost > 10:
    break

  for i in range(4):
    nrx, nry, rcost = move(rx, ry, dx[i], dy[i])
    nbx, nby, bcost = move(bx, by, dx[i], dy[i])
    if board[nbx][nby] != 'O':
      if board[nrx][nry] == 'O':
        print(cost)
        success = True
        break
      if nrx == nbx and nry == nby:
        if rcost > bcost:
          nrx -= dx[i]
          nry -= dy[i]
        else:
          nbx -= dx[i]
          nby -= dy[i]
      if not visited[nrx][nry][nbx][nby]:
        visited[nrx][nry][nbx][nby] = True
        q.append((nrx, nry, nbx, nby, cost + 1))

if not success:
  print("-1")
