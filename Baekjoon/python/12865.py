
# n은 물건 수, k는 무게 수
n, k = map(int, input().split())
knapsack = [[0] * (k+1) for _ in range(n+1)]
items = [[0, 0]]

for _ in range(n):
  items.append(list(map(int, input().split())))

"""

  limit   0  1  2  3  4  5  6  7
  iw iv  
  6  13      0  0  0  0  0 13 13
  4  8       0  0  0  8  8 13 13
  3  6       0  0  6  8  8 13 14
  5  12      0  0  6  8 12 13 14

"""

for i in range(1, n + 1):
  for j in range(1, k + 1):
    # 현재 item의 무게와 가치 가져오기
    weight = items[i][0]
    value = items[i][1]

    if j < weight:
      # 만약 현재 가방 한계 j가 item을 못견디는 경우
      knapsack[i][j] = knapsack[i-1][j]
    else:
      # 이번 물건 제외 무게
      except_value = knapsack[i-1][j]
      # 이번 물건 포함 무게
      # 이번 물건의 무게를 뺀 값을 가져오면
      #   현재 가방 한계 - 이번 물건 무게
      # 이번 물건을 담고, 가장 많이 담을 수 있는 무게 가져옴
      conclude_value = knapsack[i-1][j-weight] + value
      knapsack[i][j] = max(except_value, conclude_value)

print(knapsack[n][k])