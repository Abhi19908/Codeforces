t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    e,o = 0,0
    for i in range(2 * n):
        if l[i] % 2 == 0:
            e += 1
        else:
            o += 1
    print("Yes" if e == o else "No")