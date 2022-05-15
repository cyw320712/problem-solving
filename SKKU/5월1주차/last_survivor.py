from collections import deque
import sys

input_file = open(sys.argv[1], 'r')
n = int(input_file.readline().rstrip())
queue = deque(map(int, input_file.readline().split()))
input_file.close()

while len(queue) > 1:
  cur = queue.popleft()
  cur_len = len(queue)
  rotate_val = cur % cur_len
  queue.rotate(-rotate_val)

output_file = open("2017312222_output.txt", 'w')
output_file.write(str(queue.pop()))
output_file.close()