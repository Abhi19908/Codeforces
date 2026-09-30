t = int(input())
for _ in range(t):
    a,b,c,n = map(int,input().split())
    m = max(a,b,c)
    c = (m - a) + (m - b) + (m - c)
    if c > n:
        print("NO")
    else:
        n -= c
        if n % 3 == 0:
            print("YES")
        else:
            print("NO")