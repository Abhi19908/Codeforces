n,m = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
s = 0
for i in range(m):
    if l[i] > 0:
        break
    s += l[i]
print(-s)