origin = input()
n = len(origin)
dp = [[False for j in range(n)] for i in range(n)]
# dp[i][j] = i부터 j까지가 팰린드롬인지 아닌지
result = [2500] * (n+1)
result[n] = 0

for i in range(n):
    dp[i][i] = 1
for i in range(1, n):
    if origin[i-1] == origin[i]:
        dp[i-1][i] = 1

for length in range(3, n+1):
    # 3부터 n까지 길이를 보면서 팰리드롬인지 확인
    # 처음와 끝이 같고, 그 사이가 팰린드롬이면 팰린드롬
    for left in range(n-length+1):
        if origin[left] == origin[left+length-1] and dp[left+1][left+length-2]:
            dp[left][left+length-1] = 1

for end in range(n):
    for start in range(end+1):
        if dp[start][end]:
            # 가능하면 해당 길이의 팰린드롬을 넣을지 뺄지로 고민
            result[end] = min(result[end], result[start-1]+1)
        else:
            # 불가능하면 str[end]를 포함하기 vs 안하기 중 작은거 넣기
            result[end] = min(result[end], result[end-1]+1)

print(result[n-1])