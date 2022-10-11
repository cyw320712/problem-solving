
from bisect import bisect_left
from itertools import combinations


language = ["cpp", "java", "python"]
job = ["backend", "frontend"]
year = ['junior', 'senior']
soulFood = ['chicken', 'pizza']

def solution(info, query):
    answer = []
    info_dict = {}

    for one in info:
        oneList = one.split()
        key = oneList[:-1]
        value = int(oneList[-1])

        for j in range(5):
            for c in combinations(key, j):
                temp = ''.join(c)
                if temp in info_dict:
                    info_dict[temp].append(value)
                else:
                    info_dict[temp] = [value]
    
    for k in info_dict:
        info_dict[k].sort()

    for one in query:
        oneList = one.split('')
        key = oneList[:-1]
        value = int(oneList[-1])

        while 'and' in key:
            key.remove('and')
        while '-' in key:
            key.remove('-')
        
        key = ''.join(key)

        if key in info_dict:
            scores = info_dict[key]

            if scores:
                enter = bisect_left(scores, value)
                answer.append(len(scores) - enter)
            else:
                answer.append(0)
    
    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))