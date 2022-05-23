import sys

n = int(sys.stdin.readline().rstrip())
cost = []

for i in range(0, n):
  line = list(map(int, sys.stdin.readline().split()))
  cost.append(line)

#####
# cost = 각 집으로 가는 R, G, B 코스트
# cost = [[R, G, B], [R, G, B]]
# cost를 해당 집으로 가는 길을 R, G, B로 선택했을 때의 최소값의 배열이라 생각
#####

for i in range(1, n):
  cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
  cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
  cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[n-1][0], cost[n-1][1], cost[n-1][2]))