def solution(skill, skill_trees):
    answer = 0
    skill_max = len(skill)
    for skill_tree in skill_trees:
        skillPointer = 0
        flag = True
        for sp in skill_tree:
            if sp in skill and sp != skill[skillPointer]:
                flag = False
            elif sp == skill[skillPointer]:
                skillPointer += 1
            
            if skillPointer == skill_max:
                break
        
        if flag: answer += 1

    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))