from queue import PriorityQueue
import sys

q = PriorityQueue()
n = int(sys.stdin.readline())

for _ in range(n):
  num = int(sys.stdin.readline())
  if num == 0:
    if q.empty():
      print(0)
    else:
      print(q.get())
  else:
    q.put(num)