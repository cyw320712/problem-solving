n, m = map(int, input().split())
candidate = list(map(int, input().split()))
candidate.sort()
cur = []
visited = [0] * (n)

def backtrack(num):
    if len(cur) == m:
        print(" ".join(map(str, cur)))
        return
    
    for i in range(num, n):
        cur.append(candidate[i])
        backtrack(i)
        cur.pop()

backtrack(0)