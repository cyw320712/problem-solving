from collections import deque

def Rotate(rc, count):
	row = len(rc)
	col = len(rc[0])
	q = deque([0] * (2*(row+col)-4))
	result = rc

	# 테두리를 하나씩 담기
	for i in range(0, col):
		q.append(rc[0][i])
	for i in range(1, row):
		q.append(rc[i][col-1])
	for i in range(col-2, 0, -1):
		q.append(rc[row-1][i])
	for i in range(row-1, 0, -1):
		q.append(rc[i][0])
	q.rotate(count)

	# 테두리에 하나씩 꺼내기
	for i in range(0, col):
		result[0][i] = q.popleft()
	for i in range(1, row):
		result[i][col-1] = q.popleft()
	for i in range(col-2, 0, -1):
		result[row-1][i] = q.popleft()
	for i in range(row-1, 0, -1):
		result[i][0] = q.popleft()
	return result

def ShiftRow(rc, count):
	rc = deque(rc)
	rc.rotate(count)
	return rc

def solution(rc, operations):
	i=0

	while i < len(operations):
		count = 1

		while i + count < len(operations) - 1:
			if operations[i+count] != operations[i]:
				break
			count += 1
		
		if operations[i] == "Rotate":
			rc = Rotate(rc, count)
		else:
			rc = ShiftRow(rc, count)
		i += count
	
	return list(rc)