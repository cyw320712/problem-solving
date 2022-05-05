import sys

n, s = map(int, sys.stdin.readline().split())
input_sequence = list(map(int, sys.stdin.readline().split()))
global result
result = 0

def backtrack(cur, total):
  if cur == n:
    if total == s:
      global result
      result +=1 
    return
  
  # 더할지 말지만 고려해주면 됨
  backtrack(cur+1, total)
  backtrack(cur+1, total+input_sequence[cur])

backtrack(0, 0)
if s == 0:
  result -= 1
print(result)
