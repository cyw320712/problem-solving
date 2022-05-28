import sys
n = int(input())
arr = list(map(int, sys.stdin.readline().split()))

cum = [-1000]*n
cum[0] = arr[0]
for i in range(1, n):
  if cum[i-1] < 0:
    cum[i] = arr[i]
  else:
    cum[i] = cum[i-1] + arr[i]

print(max(cum))