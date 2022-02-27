import sys
from collections import deque

n, k = sys.stdin.readline().rsplit()
n = int(n)
k = int(k)

victim = deque(i+1 for i in range(n))
# deque == bidirectional Queue
Josephus = []

for i in range(n):
    victim.rotate(-k + 1)
    # K+1만큼 왼쪽으로 회전(가장 왼쪽에 대상자가 오도록)
    Josephus.append(victim.popleft())

# 출력부
print("<", end="")
print(*Josephus, sep=", ", end="")
print(">")