import sys

num = int(sys.stdin.readline().rstrip())
result = []

for _ in range(num):
    x, y = sys.stdin.readline().rstrip().split()
    x = int(x)
    y = int(y)
    result.append((x, y))

result.sort(key=lambda x:(x[0], x[1]))
# 다중 조건으로 정렬하는 방법. sort 함수 사용 및 동작 방법에 대해서 조사해보자.

for i in result:
    print(i[0], i[1])