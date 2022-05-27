from bisect import bisect, bisect_left
import sys


n = int(input())
seq = list(map(int, sys.stdin.readline().split()))

dp = [seq[0]]
for i in range(n):
  if seq[i] > dp[-1]:
    # 가장 큰 수보다 더 큰 경우에만 dp에 추가
    dp.append(seq[i])
  else:
    # dp에서 seq[i]가 들어갈 자리를 이진 탐색으로 찾기
    index = bisect_left(dp, seq[i])
    # 이후 해당 자리를 대체
    dp[index] = seq[i]

print(len(dp))