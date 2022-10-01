n, b, c = map(int, input().split())

factory = list(map(int, input().split()))
cost = [0] * n
result = 0
if ( b <= c):
  for i in range(0, n):
    result += b * factory[i]

else:
  result = b * factory[0]

  for i in range(1, n):
    m = min(factory[i], factory[i-1])
    factory[i] -= m
    cost[i] += m
    result += c * m

    m = min(factory[i], cost[i-1])
    factory[i] -= m
    result += c * m

    result += b * factory[i]

print(result)
