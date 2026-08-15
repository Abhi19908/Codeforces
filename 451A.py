n,m = map(int, input().split())
tot = n * m
f = 0
while tot >= 1:
    n -= 1 
    m -= 1
    tot = n * m
    f += 1

if f & 1:
    print("Akshat")
else:
    print("Malvika")