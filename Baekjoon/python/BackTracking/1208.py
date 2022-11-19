from collections import defaultdict
n, s = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

sub = defaultdict(int)
result = 0

# 절반 이상의 집합에서 나올 수 있는 모든 합 구하기
def rightSeq(mid, sum) :
    if mid == n:
        sub[sum] += 1
        return
    
    rightSeq(mid+1, sum+nums[mid])
    rightSeq(mid+1, sum)

# 절반 이하의 집합에서 나올 수 있는 모든 합 구하기
def leftSeq(st, sum):
    if st == n//2:
        # sum은 절반 이하, s-sum은 절반 이상
        # 즉, 둘 다 있다면 s를 만들 수 있는 수열임
        # 이렇게 개수를 더해주면 된다.
        result += sub[s-sum]
        return
    
    leftSeq(st+1, sum+nums[st])
    leftSeq(st+1, sum)

rightSeq(n//2, 0)
leftSeq(0, 0)

if not s :
    # 0이라면, 아무것도 포함하지 않은 공집합인 경우를 빼줘야됨
    print(result - 1)
else:
    print(result)