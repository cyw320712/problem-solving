T = int(input())

for _ in range(T):
  n = int(input())
  coins = list(map(int, input().split()))
  target = int(input())
  knapsack = [[0] * (target+1) for _ in range(n+1)]
  
  