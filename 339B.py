n,m  = map(int, input().split())
l = list(map(int, input().split()))
c = l[0] - 1
for i in range(1,m):
    if l[i] < l[i-1]:
        c += l[i] + (n - l[i-1])
    else:
        c += l[i] - l[i-1]
print(c)