num = int(input())

time = list(map(int, input().split()))

time.sort()

result = 0
weight = len(time)

for t in time:
  result += weight * t
  weight -= 1

print(result)