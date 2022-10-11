# My Solution
def solution(id_list, report, k):
    answer = []
    reported_count = {x : 0 for x in id_list}
    reporter_list = {x : set() for x in id_list}
    result_count = {x : 0 for x in id_list}
    
    for record in report:
        reporter = record.split(" ")[0]
        reported = record.split(" ")[1]
        before = len(reporter_list[reporter])
        reporter_list[reporter].add(reported)
        after = len(reporter_list[reporter])
        if before != after:
            reported_count[reported] += 1
    
    for user in reported_count.keys():
        if reported_count[user] >= k:
            for reporter in reporter_list.keys():
                if user in reporter_list[reporter]:
                    result_count[reporter] += 1
    
    for item in result_count.values():
        answer.append(item)
    
    return answer

# Good Solution
def good_solution(id_list, report, k):
    answer = [0] * len(id_list)
    reported = {x:0 for x in id_list}

    for record in set(report):
        reported[record.split()[1]] += 1
    
    for record in set(report):
        if reported[record.split()[1]] >= k:
            answer[id_list.index(record.split()[0])] += 1
    
    return answer