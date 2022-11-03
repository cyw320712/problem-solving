n = int(input())

primes = [False, False] + [True] * (n-1)
lst = [0]
# 누적합으로 미리 값을 계산해둬야 시간초과가 안남

for i in range(2, n+1):
    if primes[i]:
        lst.append(lst[-1] + i)

        j = 2
        while i*j <= n:
            primes[i*j] = False
            j += 1

front, back = 0, 1
count = 0

while back < len(lst):
    total = lst[back] - lst[front]

    if total < n:
        back += 1
    elif total > n:
        front += 1
    else:
        count += 1
        front += 1
        back += 1

print(count)