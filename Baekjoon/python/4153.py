edges = list(map(int, input().split()))

while 0 not in edges:
    max = 0
    sum = 0

    for i in edges:
        if i > max:
            max = i
    for i in edges:
        if i != max:
            sum = sum + i*i
    if max*max == sum:
        print("right")
    else:
        print("wrong")
    edges = list(map(int, input().split()))
