n = int(input())
l = list(map(int, input().split()))
c,m = 0,0
for i in range(1,n):
    if l[i] > l[i-1]:
        c += 1
    else:
        m = max(m,c)
        c = 0 
m = max(m,c)
print(m+1)