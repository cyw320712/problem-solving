def solution(alp, cop, problems):
    max_alp = max(x[0] for x in problems)
    max_cop = max(x[1] for x in problems)

    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    knapsack = [[10001] * (max_cop + 1) for _ in range(max_alp + 1)]
    knapsack[alp][cop] = 0

    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            if i + 1 <= max_alp:
                knapsack[i+1][j] = min(knapsack[i+1][j], knapsack[i][j] + 1)
            if j + 1 <= max_cop:
                knapsack[i][j+1] = min(knapsack[i][j+1], knapsack[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp = min(max_alp, i + alp_rwd)
                    next_cop = min(max_cop, j + cop_rwd)
                    knapsack[next_alp][next_cop] = min(knapsack[next_alp][next_cop], knapsack[i][j] + cost)
    
    return knapsack[-1][-1]

print(solution(10, 10, [[10,15,2,1,2],[20,20,3,3,4]]))