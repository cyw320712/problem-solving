import sys
from collections import deque

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def radix():
    large = max(arr)
    digit = 1
    index = [0 * i for i in range(n)]
    b = [0 * i for i in range(n)]

    while int(large / digit) > 0:
        bucket = [0 * i for i in range(20)]

        for i in range(n):
            # To consider negative numbers
            # convert the range ( -9 ~ 9 ) to range (0 ~ 18)
            if arr[i] < 0:
                temp = arr[i] * -1
                index[i] = 9 - temp // digit % 10
            else:
                index[i] = arr[i] // digit % 10 + 9
            
            bucket[index[i]] += 1
        
        for i in range(1, 19):
            bucket[i] += bucket[i-1]
        
        # print(bucket)
        for i in range(n-1, -1, -1):
            b[bucket[index[i]]-1] = arr[i]
            bucket[index[i]] -= 1
        
        for i in range(n):
            arr[i] = b[i]
        
        digit *= 10

radix()
print(arr)