import sys
sys.setrecursionlimit(100000)

def solution(k, room_number):
    answer = []
    rooms = {}

    for rn in room_number:
        answer.append(find(rn, rooms))
    return answer

def find(number, rooms):
    if number not in rooms:
        rooms[number] = number + 1
        return number
    
    empty = find(rooms[number], rooms)
    rooms[number] = empty + 1
    return empty

print(solution(10, [1,3,4,1,3,1]))