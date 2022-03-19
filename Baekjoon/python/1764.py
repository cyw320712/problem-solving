import sys

n, m = map(int, sys.stdin.readline().split())

not_listen = set()
not_see = set()

for _ in range(n):
    not_listen.add(sys.stdin.readline().split()[0])
for _ in range(m):
    not_see.add(sys.stdin.readline().split()[0])

not_ls = sorted(list(not_listen & not_see))
# set의 교집합 == 듣보잡 list

print(len(not_ls))
for i in not_ls:
    print(i)