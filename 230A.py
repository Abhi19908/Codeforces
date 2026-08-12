s,n = map(int,input().split())
l = []
for _ in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
l.sort()
f = True
for p in l:
    if s > p[0]:
        s += p[1]
    else:
        f = False
        break
print("YES" if f else "NO")