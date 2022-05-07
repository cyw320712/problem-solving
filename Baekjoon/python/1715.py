from queue import PriorityQueue
import sys


n = int(input())

q = PriorityQueue()
for _ in range(n):
  q.put(int(sys.stdin.readline().strip()))

cost = 0
while q.qsize() > 1:
  first = q.get()
  second = q.get()
  cost += first + second
  q.put(first + second)

print(cost)