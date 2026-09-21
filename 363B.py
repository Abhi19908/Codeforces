n,k = map(int,input().split())
l = list(map(int,input().split()))
c = 0
s = sum(l[i] for i in range(k))
m = s #basic sliding window pattern
for i in range(1,n-k+1):
    s -= l[i-1] 
    s += l[i+k-1]
    if s < m:
        m = s
        c = i
print(c+1)