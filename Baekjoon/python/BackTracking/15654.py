n, m = map(int, input().split())
candidate = list(map(int, input().split()))
candidate.sort()
cur = []
visited = [0] * (n)

def backtrack():
    if len(cur) == m:
        print(" ".join(map(str, cur)))
        return
    
    for i in range(0, n):
        if visited[i] == 0:
            visited[i] = 1
            cur.append(candidate[i])
            backtrack()
            cur.pop()
            visited[i] = 0

backtrack()