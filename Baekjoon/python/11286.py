import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
heap = []

for _ in range(n):
    num = int(input())

    if num == 0:
        try:
            print(heappop(heap)[1])
        except:
            print(0)
    else:
        heappush(heap, (abs(num), num))