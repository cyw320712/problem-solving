import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
lis = [nums[0]]
pre = [0] * (n)
# 이전 값을 추적하기 위한 배열

for i, num in enumerate(nums[1:], start=1):
    # dp의 가장 마지막 원소보다 큰 경우 맨 마지막에 추가
    if lis[-1] < num:
        lis.append(num)
        pre[i] = len(lis) - 1
    # 그게 아니라면 들어갈 위치를 이분탐색으로 정하기
    else:
        left = 0
        right = len(lis)

        while left < right:
            mid = (left + right) // 2

            if lis[mid] < num:
                left = mid + 1
            else:
                right = mid
        
        lis[right] = num
        pre[i] = right
    # 최대 n번의 log(n) 이분탐색 수행 == nlogn LIS

print(len(lis))
answer = []
total = len(lis) - 1
for i in range(n-1, -1, -1):
    if pre[i] == total:
        answer.append(nums[i])
        total -= 1
answer.reverse()
print(* answer)