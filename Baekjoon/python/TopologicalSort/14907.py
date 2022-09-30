from collections import defaultdict, deque

queue = deque()
time = []
graph = defaultdict(list)
dp = []
inDegree = defaultdict(list)

while True:
    try:
        string = input()
    except:
        break
    
    query = string.split()
    
    if len(query) == 2:
        x, t = query[0], int(query[1])
        queue.append(x)
        time.append(t)
    elif len(query) == 3:
        x, y, t = query[2], query[0], int(query[1])
        for s in x:
            graph[s].append(y)
        time.append(t)
        inDegree[y] = len(x)
    else:
        break

dp[:] = time[:]

while queue:
    cur = queue.popleft()
    curIndex = ord(cur) - 65

    for next in graph[cur]:
        inDegree[next] -= 1
        nextIndex = ord(next) - 65

        dp[nextIndex] = max(dp[curIndex] + time[nextIndex], dp[nextIndex])
        if not inDegree[next]:
            queue.append(next)

print(max(dp))