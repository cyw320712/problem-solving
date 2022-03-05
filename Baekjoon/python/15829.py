import sys

num = int(sys.stdin.readline())
string = sys.stdin.readline().rstrip()

result = 0
count = 0

for i in string:
    temp = ord(i)-96
    for i in range(0, count):
        temp *= 31
    count +=1
    result += temp

print(result%1234567891)