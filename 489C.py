m,s = map(int,input().split())
if s == 0 and m == 1:
    print("0 0")
elif s > 9 * m or s == 0: 
    print("-1 -1")
else:
    b = ""
    l = s
    for i in range(m):
        d = min(9,l)
        b += str(d)
        l -= d
        #print(d,l,b)
    sm = ""
    l = s - 1
    for i in range(m - 1):
        d = min(9,l)
        sm = str(d) + sm
        l -= d
    sm = str(l + 1) + sm
    print(sm,b)