n = int(input())
l = list(map(int,input().split()))
m = 0
c = 1
for i in range(n-1):
    if l[i+1] < l[i]:
        m = max(m,c)
        c = 0
    c += 1
m = max(m,c)
print(m)