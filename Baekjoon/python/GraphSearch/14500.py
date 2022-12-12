n, m = map(int, input().split())
result = 0
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def dfs(x, y, total, size):
    global result
    if size == 4:
        result = max(result, total)
        return
    
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny]: continue

            if size == 2:
                visited[nx][ny] = 1
                dfs(x, y, total + board[nx][ny], size + 1)
                visited[nx][ny] = 0
            
            visited[nx][ny] = 1
            dfs(nx, ny, total + board[nx][ny], size + 1)
            visited[nx][ny] = 0

for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, board[i][j], 1)
        visited[i][j] = 0
        
print(result)