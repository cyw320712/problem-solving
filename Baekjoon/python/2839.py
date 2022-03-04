import sys

num = int(sys.stdin.readline())
count = []
count.append(0)
count.append(-1)
count.append(-1)
count.append(1)
count.append(-1)
count.append(1)

for i in range(6, num+1):
    if count[i-3] != -1 and count[i-5] != -1:
        count.append(min(count[i-3], count[i-5])+1)
    elif count[i-3] != -1:
        count.append(count[i-3] + 1)
    elif count[i-5] != -1:
        count.append(count[i-5] + 1)
    else:
        count.append(-1)

print(count[num])