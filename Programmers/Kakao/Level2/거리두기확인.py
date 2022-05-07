from collections import deque


def solution(places):
    answer = []

    for board in places:
      target = deque()
      for i in range(5):
        line = board[i]
        for j in range(5):
          if line[j] == "P":
            target.append((i, j, 0))
      
      dx = [-1, 0, 1, 0]
      dy = [0, -1, 0, 1]
      flag = True
      for i in range(len(target)):
        cur = target.popleft()
        visited = [[0]*5 for _ in range(5)]
        q = deque()
        q.append(cur)
        visited[cur[0]][cur[1]] = 1
        while q:
          cx, cy, cc = q.popleft()
          # print(f"({cx}, {cy}, [{board[cx][cy]}]), cost: {cc}")
          for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            nc = cc + 1
            
            if 0<= nx < 5 and 0<= ny < 5:
              if not visited[nx][ny]:
                if nc <= 2 and board[nx][ny] == 'P':
                  flag = False
                  break
                elif board[nx][ny] == 'P':
                  q.append((nx, ny, 0))
                  visited[nx][ny] = 1
                elif board[nx][ny] == 'O':
                  q.append((nx, ny, nc))
                  visited[nx][ny] = 1
      
      if flag:
        answer.append(1)
      else:
        answer.append(0)

    return answer

places = [["PXXXX", "XPXXX", "XXXXX", "XXXXX", "XXXXX"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))