t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    m = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            m = min(m, abs(l[i]-l[j]))
    print(m)