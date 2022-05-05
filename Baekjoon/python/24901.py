n = int(input())

i = 0
result = ""
while i ^ n != 0:
  result += str(format(i, 'b'))
  i += 1
result += str(format(i, 'b'))
print(result)
