n = int(input())
l = list(map(int, input().split()))
s = sorted(l)
d = {}
for i in range(n):
    d[s[i]] = i
for i in range(n):
    l[i] = d[l[i]]
q,r = -1,-1
for i in range(n):
    if l[i] != i:
        q = i
        break
for i in range(n-1, -1, -1):
    if l[i] != i:
        r = i
        break
if q == -1 or r == -1:
    print("yes")
    print(1, 1)
else:
    l = l[:q] + l[q:r+1][::-1] + l[r+1:]
    f = True
    for i in range(q, r+1):
        if l[i] != i:
            f = False
            break
    if f:
        print("yes")
        print(q+1, r+1)
    else:
        print("no")