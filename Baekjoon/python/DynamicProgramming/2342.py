import sys
input = sys.stdin.readline

def move(depart, dest):
    if depart == dest:
        return 1
    elif depart == 0 or dest == 0:
        return 2
    elif depart % 2 != dest % 2:
        return 3
    else:
        return 4

seq = list(map(int, input().split()))
seq.pop()

# dp[i][l][r] = l과 r을 각각 의 위치에 발을 뒀을 때 최소값
dp = [[[400001] * 5 for _ in range(5)] for _ in range(len(seq)+1)]
dp[-1][0][0] = 0

for i in range(len(seq)):
    # 왼발 움직이기
    for r in range(5): # 각 오른발 위치에 대해서
        for k in range(5): # 왼발이 k에 있었다면?
            dp[i][seq[i]][r] = min(dp[i][seq[i]][r], dp[i-1][k][r] + move(k, seq[i]))
    
    # 오른발 움직이기
    for l in range(5): # 각 왼발 위치에 대해서
        for k in range(5): # 오른발이 k에 있었다면?
            dp[i][l][seq[i]] = min(dp[i][l][seq[i]], dp[i-1][l][k] + move(k, seq[i]))

m = 400001
for l in range(5):
    for r in range(5):
        m = min(m, dp[len(seq) - 1][l][r])
print(m)