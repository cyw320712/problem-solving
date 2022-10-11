def validateNumber(stones, k, children):
    count = 0

    # count는 건너 뛰어야하는 돌의 개수
    for stone in stones:
        if stone - children < 0:
            # 못 건너는 경우
            count += 1
        else:
            # 건널 수 있으면 초기화
            count = 0
        
        if count == k:
            # 못 건너는 돌의 개수가 k개라면 false
            return False
    
    return True


def solution(stones, k):
    answer = 0

    front, end = 1, 200000000

    # 이분 탐색
    while front <= end:
        mid = (front + end) // 2

        if validateNumber(stones, k, mid):
            answer = max(answer, mid);
            front = mid + 1
        else:
            end = mid - 1
    
    return answer