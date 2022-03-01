import sys
from collections import Counter

num = int(sys.stdin.readline())

sum = 0
max = -4000
min = 4000
appear = []
counter = {}

for _ in range(num):
    temp = int(sys.stdin.readline())
    sum += temp
    appear.append(temp)
    if max < temp: max = temp
    if min > temp: min = temp
    if temp not in counter:
        counter[temp] = 0
    counter[temp] += 1

print(round(sum/num))
# average

appear.sort()
print(appear[int(num/2)])
# middle value

c = Counter(appear)
if len(appear) == 1:
    print(appear[0])
else:
    first, second = c.most_common(2)
    if second[1] == first[1]:
        print(second[0])
    else:
        print(first[0])
# mode

print(max - min)
# range