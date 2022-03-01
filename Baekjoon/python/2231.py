import sys
from math import log10, floor

num = int(sys.stdin.readline())

if num == 1:
    print(0)
elif 1 < num <= 9:
    flag = False
    for i in range(1, num+1):
        if i*2 == num:
            print(i)
            flag = True
            break
    if flag == False:
        print(0)
else:
    digit = floor(log10(num)) + 1
    flag = False
    temp = num
    for i in range(temp-digit*9, temp+1):
        result = i
        sum = i
        while True:
            if i < 10:
                sum += i
                break
            sum += i%10
            i = int(i/10)
        
        if sum == temp:
            print(result)
            flag=True
            break

    if flag == False:
        print(0)
