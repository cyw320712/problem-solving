import sys

standard_num, standard = int(input()), list(map(int, sys.stdin.readline().split()))
weight_num, weight = int(input()), list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(40001)]
dp[0] = 1
result = []

for i in range(standard_num):
    # 모든 추에 대해서 한 번씩 넣고 빼기를 해서 가능한 것들을 저장

    for j in range(0, 40001):
        if dp[j]:
            dp[j] = 1

            # 현재 추 더하기
            dp[j + standard[i]] = 1

            # 현재 추에서 빼기
            if standard[i] - j >= 0:
                dp[standard[i] - j] = 1

            # 현재 가능 무게에서 현재 추 빼기
            elif j - standard[i] >= 0:
                dp[j - standard[i]] = 1

for w in weight:
    if dp[w]:
        result.append("Y")
    else:
        result.append("N")

print(" ".join(result))
