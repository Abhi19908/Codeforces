t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    s = sorted([a,b,c,d])
    m1,m2 = s[3],s[2]
    if (m1 in [a,b] and m2 in [a,b]) or (m1 in [c,d] and m2 in [c,d]):
        print("NO")
    else:
        print("YES")