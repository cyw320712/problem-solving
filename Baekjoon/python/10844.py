N = int(input())

dp = [[0]*10 for _ in range(N+1)]

# dp[i][j] = i자리 수중에서 마지막 수가 j인 계단 수의 수
# 0이나 9는 1개씩만 있을 수 있으니까 그냥 바로 가져오기
# 나머지는 i-1자리 수에서 j로 끝날 수 있는 계단수의 수 (j-1과 j+1)의 합

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1] 

print(sum(dp[N]) % 1000000000)