# my solution
def solution(s):
    answer = ""
    word3 = {
      "one": "1", "two":"2", "six":"6",
    }
    word4 = {
      "zero":"0", "four":"4", "five":"5", "nine":"9"
    }
    word5 = {
      "three":"3", "seven":"7", "eight":"8",
    }
    numbers = [str(i) for i in range(10)]
    i = 0
    while i < len(s):
      if i not in numbers:
        if s[i:i+3] in word3:
          answer += word3[s[i:i+3]]
          i += 3
        elif i <= len(s) -4 and s[i:i+4] in word4:
          answer += word4[s[i:i+4]]
          i += 4
        elif i <= len(s) - 5 and s[i:i+5] in word5:
          answer += word5[s[i:i+5]]
          i += 5
        else:
          answer += str(s[i])
          i += 1
    
    return int(answer)
