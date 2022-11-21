n = int(input())
INF = int(1e9)
dp = [[INF, []] for _ in range(1000001)]
dp[0] = [INF, []]
dp[1] = [0, [1]]
dp[2] = [1, [1, 2]]
dp[3] = [1, [1, 3]]

path = []
for i in range(4, n+1):
    candidates = []
    if i % 3 == 0:
        candidates.append([dp[i//3][0] + 1, dp[i//3][1] + [i]])
    if i % 2 == 0:
        candidates.append([dp[i//2][0] + 1, dp[i//2][1]+ [i]])
    candidates.append([dp[i-1][0] + 1, dp[i-1][1]+ [i]])

    min_val = INF
    min_path = []
    for j in range(len(candidates)):
        if candidates[j][0] < min_val:
            min_val = candidates[j][0]
            min_path = candidates[j][1]
    
    dp[i] = [min_val, min_path]


print(dp[n][0])
print(" ".join(map(str, list(reversed(dp[n][1])))))