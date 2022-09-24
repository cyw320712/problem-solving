import sys
input = sys.stdin.readline

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

count0 = 0
count1 = 0
count2 = 0

def recursion(x, y, size):
    global count0, count1, count2

    cur = board[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):

            if board[i][j] != cur:
                for k in range(3):
                    for l in range(3):
                        recursion(x + k * size//3, y + l * size // 3, size // 3)
                return
    
    if cur == -1:
        count0 += 1
    elif cur == 0:
        count1 += 1
    else:
        count2 += 1

recursion(0, 0, n)
print(count0)
print(count1)
print(count2)