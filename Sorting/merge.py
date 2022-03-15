import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def merge(left, mid, right):
    i = left
    j = mid+1
    k = left
    saved = [0 * i for i in range(n)]

    while i <= mid and j <= right:
        # Search two arr and save small one to sorted array(saved)
        if arr[i] <= arr[j]:
            saved[k] = arr[i]
            k += 1
            i += 1
        else:
            saved[k] = arr[j]
            k += 1
            j += 1
    
    # Save remand one to sorted array(saved)
    if i > mid:
        for l in range(j, right+1):
            saved[k] = arr[l]
            k += 1
            l += 1
    else:
        for l in range(i, mid+1):
            saved[k] = arr[l]
            k += 1
            l += 1
    
    # recall sorted saved array to main array
    for l in range(left, right+1):
        arr[l] = saved[l]

def divide(left, right):
    if left < right:
        mid = (left+right)//2
        divide(left, mid)
        divide(mid+1, right)
        merge(left, mid, right)

divide(0, n-1)

print(arr)