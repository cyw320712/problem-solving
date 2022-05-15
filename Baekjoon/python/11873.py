import sys
from collections import deque


def area(bar):
    stack = deque(maxlen=len(bar))
    max_area = 0
    
    print(bar)
    # enumerate보다 range가 더 빠르다
    for seq in range(len(bar)):
        print(stack)
        # 모노톤 스택을 유지하기
        while stack and bar[stack[-1]] > bar[seq]:
            height = bar[stack.pop()]
            # height = 현재 스택의 맨 끝 요소
            if stack:
                # stack이 남아 있다면 너비 구하기
                width = seq - stack[-1] - 1
            else:
                # 이거 하나였다면 이거 하나가 너비
                width = seq
            print(f"{seq}: {width} * {height} vs {max_area}")
            max_area = max(max_area, height * width)
        
        stack.append(seq)

    # 스택에 요소가 남은 경우
    while stack:
        height = bar[stack.pop()]
        if stack:
            width = len(bar) - stack[-1] - 1
        else:
            width = len(bar)
        print(f"remain: {width} * {height} vs {max_area}")
        max_area = max(max_area, height * width)
    print(max_area)
    return max_area


if __name__ == '__main__':
    while True:
        height, width = map(int, sys.stdin.readline().split())
        stack = [0] * width
        answer = 0  # 최대 직사각형 넓이

        # height 와 width가 모두 0인 경우
        if not (height | width):
            break
        
        for _ in range(height):
            # 한 row씩 field로 받기
            field = tuple(map(int, sys.stdin.readline().split()))
            
            # 스택에 넣기 (스택은 연속된 새로줄 길이 찾는 것)
            for i in range(width):
                stack[i] = stack[i] * field[i] + field[i]
            # 스택에서 가장 큰 직사각형 구하기
            answer = max(answer, area(stack))

        print(answer)
