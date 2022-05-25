def solution(survey, choices):
    answer = ''
    score = {1:[0, 0], 2:[0, 0], 3:[0, 0], 4:[0, 0]}
    # RT = 1, CF = 2, JM = 3, AN = 4
    reverse = ["TR", "FC", "MJ", "NA"]
    for i in range(len(survey)):
      if survey[i] in reverse:
        choices[i] = 8-choices[i]
    
    for i in range(len(survey)):
      if survey[i] == "NA" or survey[i] == "AN":
        if choices[i] > 4:
          score[4][1] += choices[i] - 4
        else:
          score[4][0] += 4 - choices[i]
      if survey[i] == "TR" or survey[i] == "RT":
        if choices[i] > 4:
          score[1][1] += choices[i] - 4
        else:
          score[1][0] += 4 - choices[i]
      if survey[i] == "CF" or survey[i] == "FC":
        if choices[i] > 4:
          score[2][1] += choices[i] - 4
        else:
          score[2][0] += 4 - choices[i]
      if survey[i] == "JM" or survey[i] == "MJ":
        if choices[i] > 4:
          score[3][1] += choices[i] - 4
        else:
          score[3][0] += 4 - choices[i]
    
    if score[1][0] < score[1][1]:
      answer += "T"
    else:
      answer += "R"
    if score[2][0] < score[2][1]:
      answer += "F"
    else:
      answer += "C"
    if score[3][0] < score[3][1]:
      answer += "M"
    else:
      answer += "J"
    if score[4][0] < score[4][1]:
      answer += "N"
    else:
      answer += "A"

    return answer
