import sys

dist = int(sys.stdin.readline())
count = int(sys.stdin.readline())

if count:
    disable = list(map(str, sys.stdin.readline().split()))
else:
    disable = []

result = abs(100 - dist)
# current channel is 100

for num in range(1000001):
    for n in str(num):
        if n in disable:
            # Possibility check
            break
    else:
        result = min(result, len(str(num)) + abs(num - dist))

print(result)