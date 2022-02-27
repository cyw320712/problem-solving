import sys
num = int(sys.stdin.readline())
# input() 대신 sys.stdin.readline() 사용하기

person = []

for _ in range(num):
    age, name = sys.stdin.readline().rstrip().split()
    age = int(age)
    person.append((age, name))
    # name이 같은 case가 있기 때문에 dictionary는 사용 불가

person.sort(key=lambda x:x[0])

for i in person:
    print(i[0], i[1])
