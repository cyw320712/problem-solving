
from itertools import accumulate


def solution(queue1, queue2):
  total = sum(queue1) + sum(queue2)
  
  if total % 2 != 0:
    return -1
  
  target = total/2
  if sum(queue1) == target:
    return 0

  concat = queue1 + queue2 + queue1 + queue2
  concat = list(accumulate(concat))
  half = len(queue1) -1
  min_cost = int(1e9)
  
  start = 0
  end = half
  while end < len(concat):
    cur = concat[end] - concat[start]
    
    if cur > target:
      start += 1
    elif cur < target:
      end += 1
    else:
      min_cost = min(min_cost, start + (end-half) + 1)
      start += 1

  if min_cost == int(1e9):
    return -1
  
  return min_cost

print(solution([1, 1, 1, 1], [1, 1, 1, 1]))