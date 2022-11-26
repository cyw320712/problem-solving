import sys
input = sys.stdin.readline

n = int(input())
num = [0] + list(map(int, input().split()))
dp = [0]

for n in num:
    # 큰 작은 경우 맨 마지막에 추가
    if dp[-1] < n:
        dp.append(n)
    # 그게 아니라면 들어갈 위치를 이분탐색으로 정하기
    else:
        left = 0
        right = len(dp)

        while left < right:
            mid = (left + right) // 2

            if dp[mid] < n:
                left = mid + 1
            else:
                right = mid
        dp[right] = n
    # 최대 n번의 log(n) 이분탐색 수행 == nlogn LIS

print(len(dp)-1)