from collections import defaultdict
n, s = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

sub = defaultdict(int)
result = 0

def rightSeq(mid, sum) :
    if mid == n:
        sub[sum] += 1
        return
    
    rightSeq(mid+1, sum+nums[mid])
    rightSeq(mid+1, sum)

def leftSeq(st, sum):
    if st == n//2:
        result += sub[s-sum]
        return
    
    leftSeq(st+1, sum+nums[st])
    leftSeq(st+1, sum)

rightSeq(n//2, 0)
leftSeq(0, 0)

if not s :
    print(result - 1)
else:
    print(result)