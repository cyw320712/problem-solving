import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t) :
    cmds = input().strip()
    n = int(input())
    arr_input = input().lstrip('[').rstrip(']\n')
    if n > 0 :
        arr = arr_input.split(',')
    else : arr = []

    lp = 0
    rp = n - 1
    length = n
    
    ptr_switch_zeroLP_oneRP = 0
    for cmd in cmds :
        if cmd == 'R' :
            ptr_switch_zeroLP_oneRP = 1 - ptr_switch_zeroLP_oneRP
        elif cmd == 'D' :
            if length > 0:
                if ptr_switch_zeroLP_oneRP :
                    rp -= 1
                else : 
                    lp += 1
                length -= 1
            else :
                print('error')
                break
    else :
        res = ""
        if length > 0 :
            new = arr[lp:rp+1]
            if ptr_switch_zeroLP_oneRP :
                new.reverse()
            res += ",".join(new)
        print("[" + res + "]")