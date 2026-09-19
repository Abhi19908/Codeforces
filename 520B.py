n,m = map(int,input().split())
c = 0 
while n < m:
    if m & 1:
        m += 1
    else:
        m //= 2
    c += 1
print(c + n - m)