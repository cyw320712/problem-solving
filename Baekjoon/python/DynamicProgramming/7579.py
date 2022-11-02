import sys
input = sys.stdin.readline

n, m = map(int, input().split())
bytes = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
total = sum(costs)
result = total

dp = [[0] *(total + 1) for _ in range(n + 1)]
# dp[i][j] == i번째 앱까지 중, j 코스트로 얻을 수 있는 최대 byte

for i in range(1, n+1):
    byte = bytes[i]
    cost = costs[i]

    for j in range(1, total+1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])
        
        if dp[i][j] >= m:
            result = min(result, j)

print(result)