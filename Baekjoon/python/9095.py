import sys

dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4
for i in range(4, 12):
  dp[i] = dp[i-1]+dp[i-2]+dp[i-3]

n = int(sys.stdin.readline().rstrip())

for _ in range(n):
  num = int(sys.stdin.readline().rstrip())
  print(dp[num])