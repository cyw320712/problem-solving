def compress(s, n):
    start = 0
    prev = s[start:start+n]
    cur_count = 1
    result = ""
    while start <= len(s)-n:
        start += n
        if prev != s[start:start+n]:
            if cur_count > 1:
                result += str(cur_count) + prev
                cur_count = 1
            else:
                result += prev
            prev = s[start:start+n]
        else:
            cur_count += 1
    result += s[start:]
    return len(result)


def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2+1):
        length = compress(s, i)
        if answer >= length:
            answer = length
    return answer

s = input()
print(solution(s))