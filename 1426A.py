t = int(input())
for _ in range(t):
    n,x = map(int, input().split())
    c = 1
    if n <= 2:
        print(1)
    else:
        c = (n - 3) // x + 2
        print(c)