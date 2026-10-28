a,b = map(int, input().split())
c,s = 0,0
while a > 0:
    a -= 1
    c += 1
    s += 1
    if s >= b:
        a += 1
        s -= b
    #print(s,a)
print(c)