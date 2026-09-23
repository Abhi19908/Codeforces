from math import sqrt
t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int,input().split()))
    s = sum(l)
    f = sqrt(s) == int(sqrt(s))
    print("YES" if f else "NO")