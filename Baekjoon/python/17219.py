from re import S
import sys

n, m = map(int, sys.stdin.readline().split())

pw = {}

for _ in range(n):
    site, password = sys.stdin.readline().split()
    pw[site] = password

for _ in range(m):
    temp = sys.stdin.readline().rsplit()[0]
    print(pw[temp])
