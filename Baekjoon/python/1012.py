import sys
from collections import deque

num = int(sys.stdin.readline())
dist_x = [-1, 0, 1, 0]
dist_y = [0, 1, 0, -1]
for _ in range(num):
    m, n, k = map(int, sys.stdin.readline().split())

    board = [[0]* n for _ in range(m)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        board[x][y] = 1
    q = deque()
    result = 0

    for a in range(m):
        for b in range(n):
            if board[a][b] == 1:
                board[a][b] = 0
                q.append((a,b))
                while q:
                    x, y = q.popleft()
                    for i in range(4):
                        nx = x + dist_x[i]
                        ny = y + dist_y[i]
                        if nx < 0 or nx >= m or ny < 0 or ny >= n:
                            continue
                        if board[nx][ny]:
                            board[nx][ny] = 0
                            q.append((nx, ny))
                result += 1
    
    print(result)
