from math import ceil
n = int(input())
l = list(map(int,input().split()))
to,te,o = 0,0,0
c = 0
for i in l:
    if i == 4:
        c += 1
    elif i == 3:
        te += 1
    elif i == 2:
        to += 1
    else:
        o += 1
c += te 
o = max(0,o-te)
c += to // 2
if to & 1:
    c += 1
    o = max(0,o-2)
c += (o + 3) // 4
print(c)