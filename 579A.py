n = int(input())
c = 0
while n//2 > 0:
    if n & 1:
        c += 1
    n //= 2
print(c+1)