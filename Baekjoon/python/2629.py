import sys


standard_num, standard = int(input()), list(map(int, sys.stdin.readline().split()))
weight_num, weight = int(input()), list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(40001)]
dp[0] = 1
result = []

for i in range(standard_num):
    temp = [0 for _ in range(40001)]

    for j in range(40000, -1, -1):
        if dp[j]:
            temp[j] = 1
            temp[j + standard[i]] = 1

            if standard[i] - j >= 0:
                temp[standard[i] - j] = 1
            elif j - standard[i] >= 0:
                temp[j - standard[i]] = 1
    
    dp = temp.copy()

for w in weight:
    if dp[w]:
        result.append("Y")
    else:
        result.append("N")

print(" ".join(result))
