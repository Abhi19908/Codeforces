t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    m = 0
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1
    s = sorted([(v,k) for k,v in d.items()], reverse=True)
    m = sum([v for v,k in s[1:]])
    if m >= s[0][0]:
        print(sum(l))
    else:
        print(s[0][1] * (m + min(s[0][0] - m, 2)) + sum([k * v for v,k in s[1:]]))