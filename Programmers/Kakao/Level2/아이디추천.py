from collections import defaultdict


def getPartition(id):
    for i, char in enumerate(id):
        if 48 <= ord(char) <= 57:
            return i
    return 0

def divideId(id, partition):
    S = id[:partition] if partition != 0 else id
    N = int(id[partition:]) if partition != 0 else 0
    return S, N

def solution(registered_list, new_id):
    if new_id not in registered_list:
        return new_id
    
    new_list = []
    for id in registered_list:
        partition = getPartition(id)
        S, N = divideId(id, partition)
        new_list.append((S, N))

    new_list.sort(key=lambda x: x[1])
    id_dict = defaultdict(int)
    partition = getPartition(new_id)
    tS, tN = divideId(new_id, partition)
    id_dict[tS] = tN
    
    for S, N in new_list:
        if id_dict[S] == N:
            id_dict[S] += 1
    
    tN = id_dict[tS]
    
    return tS + str(tN)


print(solution(['a', 'a1', 'a2', 'a3', 'a4','a5','a6','a7','a8','a9', 'a10'], 'a'))