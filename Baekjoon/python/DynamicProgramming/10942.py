import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dp = [[False] * n for _ in range(n)]
# dp[i][j] = nums[i]~nums[j]가 펠린드롬인지 아닌지 여부

for i in range(n-1, -1, -1):
    for j in range(n-1, i-1, -1):
        if i == j:
            dp[i][j] = True
        elif j - i > 2:
            if nums[i] == nums[j] and dp[i+1][j-1]:
                dp[i][j] = True
        elif nums[i] == nums[j]:
            dp[i][j] = True

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    if dp[s-1][e-1]:
        print(1)
    else:
        print(0)