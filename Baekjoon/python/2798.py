n, m = input().split()
n = int(n)
m = int(m)

deck = list(map(int, input().split()))
minimal = m
result = 0
val = 0

#bruteforce
for idx in range(n):
    for jdx in range(idx+1, n):
        for kdx in range(jdx+1, n):
            val = deck[idx] + deck[jdx] + deck[kdx];
            if(minimal > m-val and m-val >= 0):
                result = val
                minimal = abs(m-val)

print(result)
