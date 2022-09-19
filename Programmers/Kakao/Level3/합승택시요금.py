from collections import defaultdict, deque
from queue import PriorityQueue


def solution(n, s, a, b, fares):
    answer = 200000001
    graph = defaultdict(list)
    for x, y, w in fares:
        graph[x].append((w, y))
        graph[y].append((w, x))

    def dijkstra(start):
        INF = 200000001
        visited = [INF] * (n+1)
        
        pq = PriorityQueue()
        pq.put((0, start))
        visited[start] = 0

        while not pq.empty():
            cur_cost, cur_node = pq.get()

            if cur_cost > visited[cur_node]:
                continue

            for cost, next_node in graph[cur_node]:
                next_cost = cost + cur_cost
                if next_cost < visited[next_node]:
                    visited[next_node] = next_cost
                    pq.put((next_cost, next_node))
        
        return visited

    dp = [[]] + [dijkstra(i) for i in range(1, n+1)]
    # print(dp)
    for i in range(1, n+1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)

    return answer

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))