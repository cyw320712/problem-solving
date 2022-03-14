import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    least = i
    
    for j in range(i, n):
        if arr[j] < arr[least]:
            least = j
    
    if i != least:
        arr[i], arr[least] = arr[least], arr[i]

print(arr)