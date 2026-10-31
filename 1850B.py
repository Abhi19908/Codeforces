t = int(input())
for _ in range(t):
    n = int(input())
    m,c,k = 0,0,0
    for i in range(n):
        a,b = map(int,input().split())
        if a <= 10:
            c = b
            m = max(m,c)
            k = i + 1 if c == m else k
    print(k)