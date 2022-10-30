n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
visited = [0] * (n+1)
cur = []
result = []

def backtracking():
    if len(cur) == m:
        temp = " ".join(map(str, cur))
        if temp not in result:
            result.append(temp)
        return
    
    for i in range(0, len(numbers)):
        if visited[i] == 0:
            visited[i] = 1
            cur.append(numbers[i])
            backtracking()
            cur.pop()
            visited[i] = 0

backtracking()

for cur in result:
    print(cur)