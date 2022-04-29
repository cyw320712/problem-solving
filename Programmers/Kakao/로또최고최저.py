def solution(lottos, win_nums):
    answer = []
    zero_num = lottos.count(0)
    same = len(set(lottos)&set(win_nums))

    answer.append(min(6, 7 - (zero_num+same)))
    answer.append(min(6, 7 - same))

    return answer