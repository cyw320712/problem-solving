from collections import deque
import sys

seq = sys.stdin.readline().split('-')

stack = deque()

for item in seq:
    cur = 0
    plus = item.split("+")
    for inner in plus:
        cur += int(inner)
    stack.append(cur)

result = stack[0]

for i in range(1, len(stack)):
    result -= stack[i]

print(result)