from collections import deque


n, m = map(int, input().split())

board = [[0]*m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = deque()
result = deque()

def backtrack(k, remain, coin):
    # k는 이동 회수, remain 보드에 있는 코인 수
    if k > 10 or remain <= 0:
        result.append(-1)
        return
    if remain == 1:
        result.append(k)
        return
    
    for i in range(4):
        cur_remain = remain
        nx0 = coin[0][0] + dx[i]
        ny0 = coin[0][1] + dy[i]
        nx1 = coin[1][0] + dx[i]
        ny1 = coin[1][1] + dy[i]

        if nx0 >= n or nx0 < 0 or ny0 >= m or ny0 < 0:
            cur_remain -=1
        elif board[nx0][ny0] == '#':
            nx0 = coin[0][0]
            ny0 = coin[0][1]
        
        if nx1 >= n or nx1 < 0 or ny1 >= m or ny1 < 0:
            cur_remain -=1
        elif board[nx1][ny1] == '#':
            nx1 = coin[1][0]
            ny1 = coin[1][1]
        
        if (nx0, ny0, nx1, ny1) not in visited:
            visited.append((nx0, ny0, nx1, ny1))
            backtrack(k+1, cur_remain, [[nx0, ny0], [nx1, ny1]])
            visited.remove((nx0, ny0, nx1, ny1))

coin = deque()
for i in range(n):
    line = input()
    for j in range(m):
        board[i][j] = line[j]
        if line[j] == 'o':
            coin.append([i, j])

backtrack(0, 2, coin)

answer = 11
for r in result:
    if r == -1:
        continue
    else:
        answer = min(answer, r)

if answer == 11:
    print(-1)
else:
    print(answer)