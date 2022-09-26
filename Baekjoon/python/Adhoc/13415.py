from collections import deque
import sys

n = int(input())
deck = list(map(int, sys.stdin.readline().split()))

k = int(input())
cmd = deque()

# 엄청 큰 오름 * 내림차순 정렬 돌리면 그 전까지의 오름 * 내림차순 정렬은 싹다 무용지물
# 즉, 실제 cmd 스택에는 자기 앞꺼 전부 보면서 자기보다 작은 오름 * 내림차순 싹다 쳐냄
# 6 -4 3 -2 는 고려하지만, 6 5 -4 3 -2는 사실 돌리면 6 -4 3 -2랑 다를게 없다. 따라서 이것도 다 쳐내기

for i in range(k):
    up, down = map(int, sys.stdin.readline().split())
    
    while cmd and abs(cmd[-1]) <= up:
        cmd.pop()
    if not cmd:
        cmd.append(up)
    elif cmd and cmd[-1] < 0:
        cmd.append(up)

    while cmd and abs(cmd[-1]) <= down:
        cmd.pop()
    if not cmd:
        cmd.append(-down)
    elif cmd and cmd[-1] > 0:
        cmd.append(-down)
cmd.append(0)
# 8개의 원소가 있을 때, 6, -4, 3, -2라고 가정하자.
# 수는 4, 1, 2, 5, 8, 7, 6, 3
# 6으로 정렬을 하면 1, 2, 4, 5, 7, 8, 6, 3. 6, 3은 건드려지지 않는다.
# -4로 정렬을 하면, 5, 4, 2, 1, 7, 8, 6, 3. 7 이후의 수는 건드려지지 않는다.
# 3으로 정렬하면, 2, 4, 5, 1, 7, 8, 6, 3. 1 이후의 수는 건드려지지 않는다.
# -2로 정렬하면, 4, 2, 5, 1, 7, 8, 6, 3. 끝난다.
# 즉, 미리 배열을 정렬해두고, 오름차순 정렬의 경우에는 뒤에서부터, 내림차순의 경우는 앞에서부터 수를 하나씩
# 넣어주면 매번 정렬을 하지 않아도 된다!

result = [0] * (n)
end = cmd.popleft()
e_value = abs(end)
asc, desc = e_value-1, 0
result[e_value:] = deck[e_value:]
deck = sorted(deck[:e_value])
# print(result)
# print(deck[:asc])
while cmd:
    cur = cmd.popleft()
    start = cur
    s_value = abs(start)
    # print(e_value, s_value, result)
    if end > 0:
        for i in range(e_value-1, s_value-1, -1):
            result[i] = deck[asc]
            asc -= 1
    else:
        for i in range(e_value-1, s_value-1, -1):
            result[i] = deck[desc]
            desc += 1

    end = start
    e_value = abs(end)

answer = ""
for i in range(len(result)):
    answer += str(result[i])
    if i < len(result) - 1:
        answer += " "

print(answer)