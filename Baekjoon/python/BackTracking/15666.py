n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
cur = []
result = []

def backtracking(num):
    if len(cur) == m:
        temp = " ".join(map(str, cur))
        if temp not in result:
            result.append(temp)
        return
    
    for i in range(num, len(numbers)):
        cur.append(numbers[i])
        backtracking(i)
        cur.pop()

backtracking(0)

for cur in result:
    print(cur)