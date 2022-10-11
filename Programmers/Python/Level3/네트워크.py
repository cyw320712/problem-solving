from collections import defaultdict


def solution(n, computers):
    answer = 0
    visited = [0] * (n+1)
    
    graph = defaultdict(list)
    for i, computer in enumerate(computers):
        for j in range(len(computer)):
            if computer[j] and i != j:
                graph[i+1].append(j+1)
    
    for i in range(1, n+1):
        if visited[i] == 1:
            continue
        answer += 1
        dfs(i, visited, graph)

    return answer

def dfs(node, visited, graph):
    if not graph[node] or visited[node]:
        return
    
    visited[node] = 1
    
    for i in graph[node]:
        dfs(i, visited, graph)

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))