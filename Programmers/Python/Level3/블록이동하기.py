
from collections import deque

def solution(board):
    answer = 0
    n = len(board)

    dirx = [-1, 0, 1, 0]
    diry = [0, -1, 0, 1]

    visited = deque()
    q = deque()
    q.append([[0, 0], [0, 1], 0])
    visited.append([[0, 0], [0, 1]])

    answer = 0
    while q:
        cur1, cur2, answer = q.popleft()
        cur1x, cur1y = cur1
        cur2x, cur2y = cur2

        # print(cur1, cur2, answer)

        if (cur1x == cur1y == n-1) or (cur2x == cur2y == n-1):
            break
                
        for i in range(4):
            next1x = cur1x + dirx[i]
            next1y = cur1y + diry[i]
            next2x = cur2x + dirx[i]
            next2y = cur2y + diry[i]

            if 0 <= next1x < n and 0 <= next1y < n and 0 <= next2x < n and 0 <= next2y < n and \
                board[next1x][next1y] == 0 and board[next2x][next2y] == 0 and [[next1x, next1y], [next2x, next2y]] not in visited:
                    q.append([[next1x, next1y], [next2x, next2y], answer + 1])
                    visited.append([[next1x, next1y], [next2x, next2y]])

        # 가로 방향
        if cur1x == cur2x:
            top = cur1x - 1
            bottom = cur1x + 1
            
            # 위 2칸이 비어있는 경우 (왼쪽으로 돌릴 수 있음)
            if 0 <= top < n and board[top][cur1y] == 0 and board[top][cur2y] == 0:
                if [[top, cur1y], [cur1x, cur1y]] not in visited:
                    q.append([[top, cur1y], [cur1x, cur1y], answer+1])
                    visited.append([[top, cur1y], [cur1x, cur1y]])
                if [[top, cur2y], [cur2x, cur2y]] not in visited:
                    q.append([[top, cur2y], [cur2x, cur2y], answer+1])
                    visited.append([[top, cur2y], [cur2x, cur2y]])
            
            
            # 아래 2칸이 비어있는 경우 (오른쪽으로 돌릴 수 있음)
            if 0 <= bottom < n and board[bottom][cur1y] == 0 and board[bottom][cur2y] == 0:
                if [[bottom, cur1y], [cur1x, cur1y]] not in visited:
                    q.append([[bottom, cur1y], [cur1x, cur1y], answer+1])
                    visited.append([[cur1x, cur1y], [bottom, cur1y]])
                if [[cur2x, cur2y], [bottom, cur2y]] not in visited:
                    q.append([[cur2x, cur2y], [bottom, cur2y], answer+1])
                    visited.append([[cur2x, cur2y], [bottom, cur2y]])
        
        # 세로 방향
        else:
            left = cur1y - 1
            right = cur1y + 1

            # 왼쪽 2칸이 모두 비어있는 경우 (위로 돌릴 수 있음)
            if 0 <= left < n and board[cur1x][left] == 0 and board[cur2x][left] == 0:
                if [[cur1x, left], [cur1x, cur1y]] not in visited:
                    q.append([[cur1x, left], [cur1x, cur1y], answer+1])
                    visited.append([[cur1x, left], [cur1x, cur1y]])
                
                if [[cur2x, left], [cur2x, cur2y]] not in visited:
                    q.append([[cur2x, left], [cur2x, cur2y], answer+1])
                    visited.append([[cur2x, left], [cur2x, cur2y]])

            # 오른쪽 2칸이 모두 비어있는 경우 (아래로 돌릴 수 있음)
            if 0 <= right < n and board[cur1x][right] == 0 and board[cur2x][right] == 0:
                if [[cur1x, cur1y], [cur1x, right]] not in visited:
                    q.append([[cur1x, cur1y], [cur1x, right], answer+1])
                    visited.append([[cur1x, cur1y], [cur1x, right]])
                
                if [[cur2x, cur2y], [cur2x, right]] not in visited:
                    q.append([[cur2x, cur2y], [cur2x, right], answer+1])
                    visited.append([[cur2x, cur2y], [cur2x, right]])

    return answer

print(solution([[0, 0, 0, 1, 1], 
 [0, 0, 0, 1, 0], 
 [0, 1, 0, 1, 1], 
 [1, 1, 0, 0, 1], 
 [0, 0, 0, 0, 0]]))