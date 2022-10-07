from collections import defaultdict, deque


K, N, F = map(int, input().split())
graph = defaultdict(list)

for _ in range(F):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = []

def backtrack(cur, friends):
    global result

    if result:
        return
    if len(friends) == K:
        result = sorted(friends)
        return
    
    for next in range(cur+1, N+1):
        if not visited[next]:
            for friend in friends:
                if friend not in set(graph[next]):
                    break
            else:
                visited[next] = 1
                backtrack(next, friends+[next])
                visited[next] = 0

for i in range(1, N+1):
    visited = [0] * (1001)
    visited[i] = 1
    backtrack(i, [i])
    if result:
        break

if not result:
    print(-1)
else:
    for a in result:
        print(a)