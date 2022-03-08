import sys

n, x, y = map(int, sys.stdin.readline().split())

result = 0
while n != 0:
    n -= 1
    
    if x < 2 ** n and y < 2 ** n:
        result += (2 ** (2* n)) * 0
    
    elif x < 2 ** n and y >= 2 ** n:
        result += (2 ** (2* n)) * 1
        y -= (2 ** n)
    
    elif x >= 2 ** n and y < 2 ** n:
        result += (2 ** (2* n)) * 2
        x -= (2 ** n)
    
    else:
        result += (2 ** (2* n)) * 3
        x -= (2 ** n)
        y -= (2 ** n)

print(result)