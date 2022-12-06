from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
pods = []

q = deque()
for i in range(n):
    for j in range(n):
        if visited[i][j]: continue
        if board[i][j] == 0: continue

        pod = 0
        q.append((i, j))
        visited[i][j] = True

        while q:
            cx, cy = q.popleft()
            pod += 1

            for k in range(4):
                nx, ny = cx + dx[k], cy + dy[k]

                if 0 <= nx < n and 0 <= ny < n:
                    if visited[nx][ny]: continue
                    if board[nx][ny] == 0: continue

                    visited[nx][ny] = True
                    q.append((nx, ny))

        pods.append(pod)

pods.sort()
print(len(pods))
for i in pods:
    print(i)
