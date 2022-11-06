import sys
sys.setrecursionlimit(100004)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = list(range(n+1))

def find(x):
    if x != parent[x]:
        # 트리 단축
        parent[x] = find(parent[x])
    return parent[x]

linked = 0
for _ in range(m):
    x, y = map(int, input().split())
    x, y = find(x), find(y)
    # 부모끼리 연결해줘야 됨

    if x != y:
        # 하나의 그룹으로 연결된 회수
        linked += 1
        parent[x] = y

# 총 그룹의 개수 찾기 (각 노드의 부모노드들만 모아서 set으로 개수 세기)
group = len(set(map(find, parent[1:])))

# 전체 링크 개수 - 연결된 링크 수 == 사이클로 연결된 개수 (끊어야 트리가 됨)
# group - 1 == 총 그룹 개수 - 1 = 그룹을 하나로 만드는데 필요한 링크 수
print(m - linked + group - 1)