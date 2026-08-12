n,a,b,c = map(int, input().split())
d = [-1] * (n + 1)
d[0] = 0
for i in range(0,n+1):
    if d[i] != -1:
        for j in (a , b , c ):
            if i + j <= n:
                d[i+j] = max(d[i+j], d[i] + 1)
print(d[n])