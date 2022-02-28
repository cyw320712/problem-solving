import sys

num = int(sys.stdin.readline())

for _ in range(num):
    h, w, n = map(int, sys.stdin.readline().rsplit())
    # map으로 한 번 에 받을 수 있음
    # 임의의 개수의 정수라면 list에 담아서 저장
    div = n//h
    ho = div + 1 # 1층부터 시작
    floor = n - div*h
    if n % h == 0:
        ho = div
        floor = h
    print(f"{floor * 100 + ho}")