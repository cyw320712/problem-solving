import sys

n = int(input())
tree = []

for i in range(n):
  tree.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, n):
  for j in range(i+1):
    if j == 0:
      tree[i][j] += tree[i-1][j]
    elif j == i:
      tree[i][j] += tree[i-1][j-1]
    else:
      if tree[i-1][j] > tree[i-1][j-1]:
        tree[i][j] += tree[i-1][j]
      else:
        tree[i][j] += tree[i-1][j-1]

print(max(tree[n-1]))