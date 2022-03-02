import sys

num = int(sys.stdin.readline())

for _ in range(num):
    K = int(sys.stdin.readline())
    N = int(sys.stdin.readline())

    sum = 0
    dp = [[0] * 15 for i in range(15)]
    
    for i in range(0, K+1):
        if i == 0:
            for j in range(1, N+1):
                dp[0][j] = j
        else:
            for j in range(1, N+1):
                for k in range(1, j+1):
                    dp[i][j] += dp[i-1][k]
    print(dp[K][N])
