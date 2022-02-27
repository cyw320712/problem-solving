import sys
N, K = sys.stdin.readline().rstrip().split()
# sys.stdin.readline() split()한 결과는 list
N = int(N)
K = int(K)

def fact(num):
    result = 1
    for i in range(1, num+1):
        result = result * i
    return result

print(int(fact(N)/(fact(K)*fact(N-K))))
