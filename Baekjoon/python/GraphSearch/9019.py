from collections import deque

t = int(input())

for _ in range(t):
    start, dist = map(int, input().split())
    visited = [0] * 10001
    
    q = deque()
    q.append((start, ""))
    visited[start] = 1

    while q:
        cur, path = q.popleft()

        if cur == dist:
            print(path)
            break
        
        # 1
        num2 = (2*cur)%10000
        if not visited[num2]:
            q.append((num2,path+"D"))
            visited[num2] = True
        # 2
        num2 = (cur-1)%10000
        if not visited[num2]:
            q.append((num2,path+"S"))
            visited[num2] = True
        # 3
        num2 = (10*cur+(cur//1000))%10000
        if not visited[num2]:
            q.append((num2,path+"L"))
            visited[num2] = True
            
        # 4
        num2 = (cur//10+(cur%10)*1000)%10000
        if not visited[num2]:
            q.append((num2,path+"R"))
            visited[num2] = True
