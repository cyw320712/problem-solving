num = int(input())

for _ in range(num):
  cur = int(input())
  if cur == 1 or cur == 2 or cur == 3 or cur == 6:
    print(0)
  elif cur==4:
    print(2)
  else:
    print(1)