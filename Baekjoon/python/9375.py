from collections import defaultdict

t = int(input())

for _ in range(t):
    clothes = defaultdict(int)

    n = int(input())
    result = 1

    for _ in range(n):
        name, kind = map(str, input().split())
        clothes[kind] += 1
    
    for kind in clothes.keys():
        result *= (clothes[kind] + 1)
    
    print(result - 1)