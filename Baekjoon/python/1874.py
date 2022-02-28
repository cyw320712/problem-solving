import sys
from collections import deque
num = int(sys.stdin.readline())

stack = deque()
# 1, 2, 3, 4, 5, 6, 7, 8 ...
result = deque()
flag = True
count = 0

for _ in range(num):
    cur = int(sys.stdin.readline())

    while count < cur:
        count += 1
        stack.append(count)
        result.append("+")
    
    if stack[-1] == cur:
        stack.pop()
        result.append("-")
    else:
        flag = False
        break

if flag:
    print(*result, sep="\n")
else:
    print("NO")