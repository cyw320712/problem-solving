import sys


n, m = map(int, input().split())

board = [[0] * n for _ in range(n)]
coldp = [[0] * n for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, input().split()))

for j in range(0, n):
    coldp[0][j] = board[0][j]
    for i in range(1, n):
        coldp[i][j] = coldp[i-1][j] + board[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    x1 -= 1
    x2 -= 1
    y1 -= 1
    y2 -= 1
    total = 0
    for i in range(y1, y2+1):
        total += coldp[x2][i]
        if x1 >= 1:
            total -= coldp[x1-1][i]
    print(total)