n = int(input())
l = list(map(int, input().split()))
s = sorted(l)
for i in range(1,n):
    l[i] += l[i-1]
    s[i] += s[i-1]
t = int(input())
for _ in range(t):
    p,lt,r = map(int, input().split())
    if p == 1:
        print(l[r-1] - l[lt-2]) if lt > 1 else print(l[r-1])
    elif p == 2:
        print(s[r-1] - s[lt-2]) if lt > 1 else print(s[r-1])