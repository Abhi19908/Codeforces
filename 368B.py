n,m = map(int,input().split())
l = list(map(int,input().split()))
d = {}
s= set()
for i in range(n,0,-1):
    s.add(l[i-1])
    d[i] = len(s)

for _ in range(m):
    k = int(input())
    print(d[k])