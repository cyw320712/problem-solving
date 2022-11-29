n = int(input())
square = [i for i in range(n+1)]

for i in range(3, n+1):
    j = 1
    val = i
    while j**2 <= i:
        val = min(val, square[i-j**2])
        j += 1
    square[i] = val + 1

print(square[n])
