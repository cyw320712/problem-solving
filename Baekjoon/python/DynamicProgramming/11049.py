n = int(input())

matrix = []

dp = [[0] * n for _ in range(n)]
# dp[i][j] == i 행렬부터 j 행렬까지 행렬곱 연산의 최소 값

for _ in range(n):
    r, c = map(int, input().split())
    matrix.append((r, c))

for i in range(1, n):
    for j in range(n-i):
        x = j+i

        dp[j][x] = 2 ** 32

        for k in range(j, x):
            dp[j][x] = min(dp[j][x],
                dp[j][k] + dp[k+1][x] + matrix[j][0] * matrix[k][1] * matrix[x][1])

# ABCDE 곱의 최소값 == 
# min(ABCDE, min(A) + min(BCDE) + 조합비용,
#            min(AB) + min(CDE) + 조합비용,
#            min(ABC) + min(DE) + 조합비용,
#            min(ABCD) + min(E) + 조합비용)

# 조합 비용은 결과를 생각해보면 됨
# ex) A와 BCDE의 조합 비용은 결국 Ar * Ac * Ec가 됨
#      A 크기 == Ar, Ac BCDE 크기 == AC * EC (안그럼 곱셈이 안되니까..)

print(dp[0][n-1])
