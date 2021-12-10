num = int(input())
result = 0

#init list for DP
fibo = list()
fibo.append(0)
fibo.append(1)

#find numth value
for idx in range(2, num+1):
    fibo.append(fibo[idx-2] + fibo[idx-1])

print(fibo[num])
