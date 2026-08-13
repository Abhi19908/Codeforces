n,k = map(int , input().split())
l = list(map(int, input().split()))
l.sort()
t = n-1
m,c = 10**6,0
for i in range(t,k):
    c = l[i] - l[i-t]
    m = min(c,m)
print(m)