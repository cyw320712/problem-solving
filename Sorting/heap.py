from ctypes.wintypes import LARGE_INTEGER
import sys
from queue import PriorityQueue
import heapq


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# STL PriorityQueue version
sort = PriorityQueue()

for item in arr:
    sort.put(item)

result = []
for _ in range(n):
    result.append(sort.get())
print(result)

# STL Heapq version
result = []
heap = []
for item in arr:
    heapq.heappush(heap, item)
# or heapq.heapify(arr) == convert arr to heap

for i in range(len(heap)):
    result.append(heapq.heappop(heap))

print(result)

# Implemented version
def heapify(unsorted, index, size):
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < size and unsorted[left_index] > unsorted[largest]:
        largest = left_index
    if right_index < size and unsorted[right_index] > unsorted[largest]:
        largest = right_index
    if largest != index:
        unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
        heapify(unsorted, largest, size)

def heap(unsorted):
    n = len(unsorted)
    for i in range(n // 2 -1, -1, -1):
        heapify(unsorted, i, n)
    for i in range(n -1, 0, -1):
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        heapify(unsorted, 0, i)
    return unsorted

print(heap(arr))