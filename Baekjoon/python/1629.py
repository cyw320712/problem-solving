a, b, c = map(int, input().split())

def divide(a, b, c):
  if b == 1:
    return a % c
  flag = False
  if b % 2==1:
    flag = True
  half = divide(a, b//2, c)
  if flag:
    return half**2 * a % c
  else:
    return half**2 % c

print(divide(a, b, c))