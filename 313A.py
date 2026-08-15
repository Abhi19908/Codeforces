n = int(input())
if(n>0):
    print(n)
else:
    l = list(str(n))
    m = max(l[-1], l[-2])
    if m == l[-1]:
        i = -1
    else:
        i = -2
    l.pop(i)
    s = ''.join(l)
    if s[1] == '0' :
        if len(s) > 2:
            s = s[0] + s[2:]
        else:
            s = 0
    print(s)