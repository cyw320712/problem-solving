from collections import deque

n, m = map(int, input().split())
board = [i for i in range(0, 101)]
visited = [0] * 101
for _ in range(n):
    depart, dist = map(int, input().split())
    board[depart] = dist
for _ in range(m):
    depart, dist = map(int, input().split())
    board[depart] = dist

q = deque()
q.append((1, 0))
visited[1] = 1

while q:
    cur, count = q.popleft()

    if cur == 100:
        print(count)
        exit()

    for i in range(1, 7):
        nxt = cur + i

        if nxt < 101:
            nxt = board[nxt]

            if not visited[nxt]:
                q.append((nxt, count+1))
                visited[nxt] = 1
