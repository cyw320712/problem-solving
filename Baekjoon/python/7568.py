times = int(input())

info = []
count = []

#======input======#
for i in range(times):
    h, w = input().split()
    h = int(h)
    w = int(w)
    info.append((h, w))
    count.append(1)

#======Ranking======#
for i in range(times):
    x, y = info[i]
    for j in range(times):
        tx, ty = info[j]
        if tx > x and ty > y:
            count[i]+=1
            
#======print======#
result = ""
for i in range(times):
    result += str(count[i])
    if i < times - 1:
        result += " "
print(result)
