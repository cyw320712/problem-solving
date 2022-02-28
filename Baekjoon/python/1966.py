import sys
from collections import deque

num = int(sys.stdin.readline())

for _ in range(num):
    size, target = map(int, sys.stdin.readline().split())

    priority = deque()
    user_input = deque(map(int, sys.stdin.readline().split()))
    printQ = deque()

    for i in range(len(user_input)):
        priority.append((user_input[i], i))
    sort_priority = deque(sorted(priority, key=lambda x:x[0], reverse=True))

    count = 0
    cur = sort_priority.popleft()
    # print(f"cur: {cur}")
    while True:
        if cur[0] != priority[0][0]:
            # print(f"Rotate: {priority[0][0]}")
            priority.rotate(-1)
        else:
            item = priority.popleft()
            # print(f"Pop: {item}")
            count += 1
            if item[1] == target:
                print(count)
                break
            cur = sort_priority.popleft()