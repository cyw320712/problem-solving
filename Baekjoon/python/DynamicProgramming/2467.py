n = int(input())
liquid = list(map(int, input().split()))

left, right = 0, n-1

result1, result2 = 0, 0

result = 2000000000

while left < right:
    sum = liquid[left] + liquid[right]

    if abs(sum) < result:
        result1 = left
        result2 = right
        result = abs(sum)
    
    if sum > 0:
        # 0보다 크면 오른쪽을 당긴다.
        right -= 1
    elif sum < 0:
        # 0보다 작으면 왼쪽을 당긴다.
        left += 1
    else:
        break

print(liquid[result1], liquid[result2])
