t = int(input())

INF = 2000000000
def bellman_ford():
    dist = [INF] * (n+1)
    dist[1] = 0

    for i in range(n):
        for edge in edges:
            cur = edge[0]
            nxt = edge[1]
            cost = edge[2]

            if dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost

                if i == n-1:
                    return True
    return False

for _ in range(t):
    n, m, w = map(int, input().split())

    edges = []
    

    for _ in range(m):
        x, y, l = map(int, input().split())
        edges.append((x, y, l))
        edges.append((y, x, l))

    for _ in range(w):
        x, y, l = map(int, input().split())
        edges.append((x, y, -l))

    if bellman_ford():
        print("YES")
    else:
        print("NO")