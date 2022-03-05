import sys

a, b, v = map(int, sys.stdin.readline().split())

result = (v-b) / (a-b)

if result == int(result):
    print(int(result))
else:
    print(int(result)+1)
