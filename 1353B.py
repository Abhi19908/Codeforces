t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    while k > 0:
        k -= 1
        if a[0] < b[-1]:
            a[0],b[-1] = b[-1],a[0]
            a.sort()
            b.sort()
        else:
            break
    print(sum(a))