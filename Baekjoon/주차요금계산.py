import math
def solution(fees, records):
    answer = []
    base_time = fees[0]
    base_cost = fees[1]
    add_time = fees[2]
    add_cost = fees[3]

    budget = {}
    in_dict = {}
    for record in records:
        sep = record.split(" ")
        hour = int(sep[0].split(":")[0])
        minute = int(sep[0].split(":")[1])
        curtime = hour*60 + minute

        car = sep[1]
        case = sep[2]

        if case == "IN":
            in_dict[car] = curtime
        else:
            try:
                temp = budget[car]
            except KeyError:
                budget[car] = 0

            budget[car] += curtime - in_dict[car]
            in_dict[car] = -1
    
    for car in in_dict.keys():
        if in_dict[car]!= -1:
            try:
                temp = budget[car]
            except KeyError:
                budget[car] = 0
            budget[car] += 1439 - in_dict[car]
    
    for car in budget.keys():
        cost = base_cost + math.ceil(max(0, budget[car]-base_time)/add_time) * add_cost
        budget[car] = cost

    sd = dict(sorted(budget.items()))
    for car in sd.keys():
        answer.append(sd[car])
    return answer