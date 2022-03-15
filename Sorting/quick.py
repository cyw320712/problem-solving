import sys
from collections import deque

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def partition(start, end):
    low = start
    high = end
    pivot = arr[start] #Standard for this sort

    while low < high:
        # Set starting position
        while low <= end and arr[low] < pivot:
            low += 1
        while high >= start and arr[high] > pivot:
            high -= 1
        
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]

    return high


def quick(start, end):
    stack = deque()
    stack.append(start)
    stack.append(end)

    while stack:
        end = stack.pop()
        start = stack.pop()
        pivot = partition(start, end)

        if pivot - 1 > start:
            stack.append(start)
            stack.append(pivot - 1)
        
        if pivot + 1 < end:
            stack.append(pivot + 1)
            stack.append(end)

quick(0, n-1)
print(arr)