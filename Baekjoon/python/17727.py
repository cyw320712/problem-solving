n = int(input())
dp = [0] * (1001)
dp[1] = 1
dp[2] = 3


for i in range(3, n+1):
  # 2칸을 채우는 방법이 2가지가 생겼으므로 2번째 전 것 * 2
  dp[i] = dp[i-1]+dp[i-2]*2

print(dp[n] % 10007)
