def isPrime(n):
  if n == 1:
    return False
  i = 2
  while i**2 <= n:
    if n%i==0:
      return False
    i+=1
  return True

def toKnary(n, k):
  result = ""
  while n:
    result += str(n%k)
    n //= k
  return result[::-1]

def solution(n, k):
  answer = 0
  knary = toKnary(n, k).split("0");
  
  for item in knary:
    try:
      item = int(item)
    except ValueError:
      continue
    
    if isPrime(item):
      answer += 1
  
  return answer