from collections import defaultdict
import math

graph = defaultdict(list)
dp = [[0, 0] for _ in range(300001)]
# [해당 노드를 포함하지 않는 경우 중 최소 cost, 해당 노드 포함하는 경우 최소 cost] 를 저장

# parent node -> child node

def solution(sales, links):
    for x, y in links:
        graph[x].append(y)
    
    dfs(sales, 1)

    return min(dp[1][0], dp[1][1])

def dfs(sales, x):
    dp[x][0] = 0
    dp[x][1] = sales[x-1]

    if not graph[x]:
        # leaf node인 경우 멈추기
        return
    
    extraCost = math.inf
    for child in graph[x]: # 4, 5
        dfs(sales, child)
        if dp[child][0] < dp[child][1]:
            dp[x][0] += dp[child][0]
            dp[x][1] += dp[child][0]
            extraCost = min(extraCost, dp[child][1] - dp[child][0]) # 그룹에서 하나는 들어가야됨
        else:
            dp[x][0] += dp[child][1]
            dp[x][1] += dp[child][1]
            extraCost = 0 # 자식 노드가 들어가면 추가로 더 넣을 필요가 없음
    
    dp[x][0] += extraCost # 부모 노드가 참석하지 않은 경우에는 반드시 추가비용을 들여서 자식노드 중 하나를 추가해줘야됨

# 답은 44
print(solution([14, 17, 15, 18, 19, 14, 13, 16, 28, 17],[[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]] ))