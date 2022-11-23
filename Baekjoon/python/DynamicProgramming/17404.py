n = int(input())

INF = int(1e9)
dist = []
result = INF

for _ in range(n):
    dist.append(list(map(int, input().split())))

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0][i] = dist[0][i]

    for j in range(1, n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + dist[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + dist[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + dist[j][2]

    for j in range(3):
        if i != j:
            result = min(result, dp[n-1][j])

print(result)