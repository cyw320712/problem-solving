str1, str2 = input(), input()
len1, len2 = len(str1), len(str2)

dp = [[[0, []] for _ in range(len2 + 1)] for _ in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j][0] = dp[i-1][j-1][0] + 1
            dp[i][j][1] = dp[i-1][j-1][1] + [str1[i-1]]
        else:
            if dp[i-1][j][0] > dp[i][j-1][0]:
                dp[i][j][0] = dp[i-1][j][0]
                dp[i][j][1] = dp[i-1][j][1]
            else:
                dp[i][j][0] = dp[i][j-1][0]
                dp[i][j][1] = dp[i][j-1][1]

print(dp[len1][len2][0])
if dp[len1][len2] != 0:
    print("".join(dp[len1][len2][1]))