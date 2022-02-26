num = int(input())

for _ in range(num):
    user_input = input()
    s = []
    flag = True
    for i in user_input:
        # list를 Stack처럼 사용하기
        if i == "(":
            s.append(i)
        else:
            if len(s) == 0:
                flag = False
                break
            temp = s.pop()
            if temp != "(" :
                flag = False
                break

    if len(s)!=0:
        # 남아있는 게 있다면
        flag = False
    if flag:
        print("YES")
    else:
        print("NO")
