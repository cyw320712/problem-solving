n = int(input())

line_visit = [0] * n
upper_visit = [0] * 40
lower_visit = [0] * 40
global result
result = 0

def backtrack(k):
  if k == n:
    global result
    result += 1
    return
  else:
    for i in range(n):
      if line_visit[i] or upper_visit[i+k] or lower_visit[k-i+n-1]:
        continue
      line_visit[i] = 1
      upper_visit[i+k] = 1
      lower_visit[k-i+n-1] = 1
      backtrack(k+1)
      line_visit[i] = 0
      upper_visit[i+k] = 0
      lower_visit[k-i+n-1] = 0

backtrack(0)
print(result)
