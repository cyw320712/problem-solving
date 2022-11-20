from collections import deque

n = int(input())
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(x, y, height, tempBoard):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    count = 0

    q.append((x, y))
    visited[x][y] = 1

    while q:
        curx, cury = q.popleft()
        count += 1

        for k in range(4):
            nextx, nexty = curx + dx[k], cury + dy[k]

            if 0 <= nextx < n and 0<= nexty < n:
                if not visited[nextx][nexty] and abs(tempBoard[curx][cury] - tempBoard[nextx][nexty]) <= height:
                    q.append((nextx, nexty))
                    visited[nextx][nexty] = 1
    
    return count


board = [list(map(int, input().split())) for _ in range(n)]
max_value = 0
edges = deque()
ending = (n*n) // 2 if n*n % 2 == 0 else (n*n) // 2 + 1

for i in range(n):
    for j in range(n):
        max_value = max(max_value, board[i][j])
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            edges.append((i, j))

min_height = max_value
left, right = 0, max_value

while left <= right:
    mid = (left + right) // 2

    tempBoard = [[board[i][j] for j in range(n)] for i in range(n)]
    tempEdges = edges.copy()
    checked = []
    count = 0

    
    for i in range(n):
        for j in range(n):
            if tempBoard[i][j] not in checked:
                checked.append(tempBoard[i][j])
                count = max(count, bfs(i, j, mid, tempBoard))

    if count < ending:
        left = mid + 1
    else:
        right = mid - 1
        min_height = min(min_height, mid)

print(min_height)