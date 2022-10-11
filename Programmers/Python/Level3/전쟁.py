from collections import defaultdict, deque

dirx = [-1, 0, 1, 0]
diry = [0, -1, 0, 1]

def solution(maps):
    answer = 0
    board = [['.'] * 1001 for _ in range(1001)]
    visited = [[0] * 1001 for _ in range(1001)]
    
    col = len(maps[0])
    row = len(maps)
    queue = deque()
    area = defaultdict(int)

    for i, line in enumerate(maps):
        for j, cell in enumerate(line):
            board[i][j] = cell
    
    for i in range(row):
        for j in range(col):
            if visited[i][j]:
                continue
            if board[i][j] == '.':
                continue
            subArea = defaultdict(int)
            queue.append([i, j])
            visited[i][j] = 1

            while queue:
                curx, cury = queue.popleft()

                subArea[board[curx][cury]] += 1

                for k in range(4):
                    nextx, nexty = curx + dirx[k], cury + diry[k]

                    if 0 <= nextx < row and 0 <= nexty < col:
                        if visited[nextx][nexty]:
                            continue
                        if board[nextx][nexty] == '.':
                            continue
                        queue.append([nextx, nexty])
                        visited[nextx][nexty] = 1
            
            subArea = dict(sorted(subArea.items(), key=lambda x: (x[1], x[0])))
            (maxCountry, maxValue) = subArea.popitem()
            totalValue = maxValue

            while subArea:
                curC, curV = subArea.popitem()
                if curV == maxValue:
                    area[curC] += curV
                else:
                    totalValue += curV
    
            area[maxCountry] += totalValue
    
    area = dict(sorted(area.items(), key=lambda x: x[1]))
    answer = area.popitem()[1]
    return answer

# print(solution(["AABCA.QA", "AABC..QX", "BBBC.Y..", ".A...T.A", "....EE..", ".M.XXEXQ", "KL.TBBBQ"]))
# print(solution(["XY..", "YX..", '..YX', '.AXY']))
print(solution(["X..X", 'X...', "....", '..YY']))