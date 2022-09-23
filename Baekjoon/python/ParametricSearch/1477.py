n, m, l = map(int, input().split())
rest = [0] + list(map(int, input().split())) + [l]
rest.sort()

start, end = 1, l-1
result = 0

while start <= end:
    count = 0
    # mid 는 얼만큼의 길이를 최소로 남길지
    mid = (start + end) // 2

    for i in range(1, len(rest)):
        if rest[i] - rest[i-1] > mid:
            # 즉, mid로 나눈 만큼 count에 더해준다.
            count += (rest[i] - rest[i-1] - 1) // mid
    
    if count > m:
        start = mid + 1
    else:
        end = mid - 1
        result = mid

print(result)
