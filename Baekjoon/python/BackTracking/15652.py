n, m = map(int, input().split())

s = []

def backtrack(num):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(num, n+1):
        s.append(i)
        backtrack(i)
        s.pop()

backtrack(1)