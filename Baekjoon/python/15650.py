import sys

n, m = map(int, sys.stdin.readline().split())
sequ = [0] * m
visit = [0] * 10
result = set()

def backtrack(k, sequ):
  if k == m:
    sequ = sorted(sequ)
    result.add(tuple(sequ))
    sequ = [0] * m
    return
  else:
    for i in range(1, n+1):
      if not visit[i]:
        sequ[k] = i
        visit[i] = 1
        backtrack(k+1, sequ)
        visit[i] = 0

backtrack(0, sequ)
result = sorted(result)
for record in result:
  for item in record:
    print(item, end=" ")
  print()