n, target = map(int, input().split())

kinds = [int(input()) for _ in range(n)]

count = 0
while n != 0 and target != 0:
    cur_val = kinds[n-1]
    if cur_val <= target:
        count += (target // cur_val)
        target -= (target // cur_val) * cur_val
    n -= 1

print(count)
