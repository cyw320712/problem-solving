one, other = input(), input()
h, w = len(one), len(other)

dp = [[0] * (w+1) for _ in range(h+1)]
# 2차원 dp를 만들어 문자가 같다면 이전 값 +1, 다르면 이전 값 중 최대값으로 저장
# 즉, dp[i][j] == one[i], other[j]까지 가장 긴 LCS의 길이를 저장한다.

for i in range(1, h+1):
    for j in range(1, w+1):
        if one[i-1] == other[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[h][w])