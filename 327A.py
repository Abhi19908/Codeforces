n = int(input())
l = list(map(int,input().split()))
s = sum(l) 
m,c = -1,0
for i in range(n):
    g = 1 if l[i] == 0 else -1
    c = max(g, c + g)
    m = max(m, c)
print(m + s)