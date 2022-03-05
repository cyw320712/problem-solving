import sys

num = int(sys.stdin.readline())
arr = []

for _ in range(num):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

arr.sort(key=lambda x:(x[1], x[0]))

for i in arr:
    print(f"{i[0]} {i[1]}")