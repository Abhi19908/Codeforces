n = int(input())
s = list(map(int, input().split()))
s.sort()
q = int(input())
for _  in range(q):
    a = int(input())
    l,r = 0,n
    while l < r:
        m = (l + r) // 2
        if s[m] <= a:
            l = m + 1
        else:
            r = m 
    print(l)
