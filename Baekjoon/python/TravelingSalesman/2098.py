import sys
input = sys.stdin.readline

n = int(input())
path = []
for _ in range(n):
    path.append(list(map(int, input().split())))

# n = 4
# path = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
dp = [[0] * (1 << n - 1) for _ in range(n)]

def solution(i, route):
    if dp[i][route] != 0:
        return dp[i][route]
    
    if route == (1 << (n-1)) -1:
        if path[i][0]:
            return path[i][0]
        else:
            return int(1e13)
    
    min_dist = int(1e13)

    for j in range(1, n):
        if not path[i][j]: continue
        if route & (1 << j-1): continue
        dist = path[i][j] + solution(j, route | (1 << (j-1)))
        min_dist = min(min_dist, dist)
    
    dp[i][route] = min_dist
    return min_dist

print(solution(0, 0))