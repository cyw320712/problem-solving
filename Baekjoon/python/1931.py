from collections import deque
import sys

n = int(input())
meeting = deque()
for _ in range(n):
  start, end = map(int, sys.stdin.readline().split())
  meeting.append((start, end))

meeting = deque(sorted(meeting, key=lambda x: (x[1], x[0])))

result = 1
prev_start, prev_end = meeting.popleft()
while meeting:
  cur_start, cur_end = meeting.popleft()
  if cur_start < prev_end:
    continue
  
  result += 1
  prev_end = cur_end


print(result)
