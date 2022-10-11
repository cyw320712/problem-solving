def solution(gems):
    kind = set(gems)
    answer = [0, len(gems)-1]
    s, e = 0, 0
    bag = {gems[s]: 1}

    while s < len(gems) and e < len(gems):
        if len(bag) < len(kind):
            # 아직 부족한 경우 e를 민다.
            e += 1
            
            if e == len(gems):
                break

            if gems[e] not in bag:
                bag[gems[e]] = 0
            bag[gems[e]] += 1

        else:
            # 얻을 수 있는 보석을 모두 얻은 경우 s를 당긴다.
            if e - s < answer[1] - answer[0]:
                answer = [s, e]
            
            if bag[gems[s]] == 1:
                bag.pop(gems[s])
            else:
                bag[gems[s]] -= 1
            s += 1
    
    answer[0] += 1
    answer[1] +=1
    return answer