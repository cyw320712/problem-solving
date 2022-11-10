t = int(input())

for _ in range(t):
    n = int(input())
    scores = []
    # scores[i] == i번째 칸까지 얻을 수 있는 최대 점수
    scores.append(list(map(int, input().split())))
    scores.append(list(map(int, input().split())))

    for i in range(1, n):
        if i == 1:
            scores[0][i] += scores[1][i-1]
            scores[1][i] += scores[0][i-1]
        else:
            scores[0][i] += max(scores[1][i-1], scores[1][i-2])
            scores[1][i] += max(scores[0][i-1], scores[0][i-2])
    print(max(scores[0][n-1], scores[1][n-1]))