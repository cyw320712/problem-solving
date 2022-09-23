n, c = map(int, input().split())

house = []

for _ in range(n):
    house.append(int(input()))

house.sort()

def validate(num, limit):
    standard = 0
    num -= 1
    for i in range(n):
        if house[i] - house[standard] >= limit:
            num -= 1
            standard = i
        if num == 0:
            break

    if num != 0:
        return False
    else:
        return True

start = 1
end = max(house)
answer = 0
while start <= end:
    mid = (start + end) // 2
    if validate(c, mid):
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)