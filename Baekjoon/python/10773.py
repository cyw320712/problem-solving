import sys
from collections import deque

num = int(sys.stdin.readline())

call = deque()
for _ in range(num):
    temp = int(sys.stdin.readline())
    if temp != 0:
        call.append(temp)
    else:
        call.pop()

result = 0
for i in call:
    result += i

print(result)