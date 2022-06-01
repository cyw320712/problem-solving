
n = int(input())
wine = [0] * (10001)
dp = [0] * (10001)

for i in range(1, n+1):
  wine[i] = int(input())

# dp = i번째 잔까지 중에서 제일 많은 양
dp[1] = wine[1]
dp[2] = dp[1] + wine[2]

for i in range(3, n+1):
  # 연속된 3개는 마실 수 없게 고려 후, 이전 dp값보다 작으면 이전 걸 그냥 가져감
  dp[i] = max(max(dp[i-3] + wine[i-1], dp[i-2]) + wine[i], dp[i-1])

print(max(dp))