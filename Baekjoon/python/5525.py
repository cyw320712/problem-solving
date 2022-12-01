n = int(input())
m = int(input())
s = input()

count = 0
pattern = 0
i = 1

while i < m -1:
    # IOI 패턴 단위로 개수 비교 == O(m)
    if s[i-1] == 'I' and s[i] == 'O' and s[i+1] == 'I':
        pattern += 1

        if pattern == n:
            pattern -= 1
            count += 1
        i += 1 # 패턴이 있다면 IO를 건너 뛰어줘야함
    else:
        pattern = 0
    i += 1

print(count)