num = int(input())
result = 0

def checker(target: int):
    res = True
    endpoint = int(target**(1/2))

    for i in range(2, endpoint+1):
        if target % i == 0:
            res = False
            break

    return res

user_input = list(map(int, input().split()))

for temp in user_input:
    if temp == 1:
        continue
    if checker(temp):
        result += 1

print(result)
