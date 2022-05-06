n = int(input())
origin = set()
two_sum = set()

for _ in range(n):
  origin.add(int(input()))

for i in origin:
  for j in origin:
    two_sum.add(i+j)

ans = []
for i in origin:
  for j in origin:
    if (i-j) in two_sum:
      ans.append(i)

ans.sort()
print(ans[-1])

