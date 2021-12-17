num = int(input())

user = []
user = list(map(int, input().split()))

#for remove duplicated
rank = list(set(user))

srank = sorted(rank)
dic = {srank[i]:i for i in range(len(srank))}

for i in user:
    print(dic[i], end = ' ')
