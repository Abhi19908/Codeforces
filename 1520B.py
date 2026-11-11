t = int(input())
for _ in range(t):
    n = int(input())
    r = 0
    p = 1
    while p <= n:
        for d in range(1,10):
            if p * d <= n:
                r += 1
        p = p * 10 + 1
    print(r)