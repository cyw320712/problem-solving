g = int(input())
p = int(input())
gates = [i for i in range(g+1)]

def find(n):
    if gates[n] == n:
        return n
    else:
        gates[n] = find(gates[n])
        return gates[n]

def union(parent, child):
    x = find(parent)
    y = find(child)
    gates[x] = y
    return

result = 0

for _ in range(p):
    flight = int(input())

    parent = find(flight)
    if parent == 0:
        break
    union(parent, parent - 1)
    result += 1

print(result)