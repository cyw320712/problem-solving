import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
shark = 2
time = 0
fishes = 0

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
x, y = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            x, y = i, j
            board[i][j] = 0
        elif board[i][j] != 0:
            fishes += 1

def findTargetFishes(x, y, size):
    targetList = []

    q = deque()
    q.append((x, y, 0))
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True

    while q:
        cx, cy, ct = q.popleft()

        for i in range(4):
            nx, ny, nt = cx + dx[i], cy + dy[i], ct + 1

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny]: continue
                if board[nx][ny] > size: continue

                visited[nx][ny] = True
                q.append((nx, ny, nt))

                if board[nx][ny] < size and board[nx][ny] != 0:
                    targetList.append((nx, ny, nt))

    return sorted(targetList, key = lambda x: (-x[2], -x[0], -x[1]))

eat = 0
time = 0
while fishes != 0:
    targets = findTargetFishes(x, y, shark)
    
    if not targets: break

    nx, ny, dist = targets.pop()

    time += dist
    board[x][y] = 0
    board[nx][ny] = 0
    eat += 1

    x, y = nx, ny

    if eat == shark:
        shark += 1
        eat = 0

print(time)