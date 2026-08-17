n,k = map(int, input().split())
l = list(map(int, input().split()))
l.sort()
m,c = 0,0
for i in range(n-1):
    c = l[i+1] - l[i]
    m = max(m,c)
f = False
if l[0] != 0 or l[-1] != k:
    m = max(l[0],k-l[-1],m/2)
    print(f'{m:.10f}')
else:
    m /= 2
    print(f'{m:.10f}')