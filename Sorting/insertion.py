import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(1, n):
    key = arr[i]
    
    j = i-1

    # key보다 큰 수는 한칸씩 옆으로 이동
    while arr[j] > key and j >= 0:
        arr[j+1] = arr[j]
        j -= 1

    # 자기 자리에 key 저장
    arr[j+1] = key

print(arr)
