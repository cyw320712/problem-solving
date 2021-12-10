from string import ascii_lowercase

times = int(input())
alpha = list(ascii_lowercase)
check_dict = {}
result = 0

while times:
    if times==0:
        break
    
    #init checking dict
    for idx in alpha:
        check_dict[idx] = 0

    flag = 1
    var = str(input())

    for idx in range(len(var)):
        # fail condition
        if(check_dict[var[idx]] == 1):
            flag=0
            break

        #end condition (for prevent idx error)
        if idx == len(var) - 1:
            break

        #if value change, check dict on
        if(var[idx]!=var[idx+1]):
            check_dict[var[idx]] = 1
    
    #success condition
    if flag == 1:
        result +=1

    times -= 1

print(result)
