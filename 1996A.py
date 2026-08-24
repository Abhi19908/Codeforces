t = int(input())
for _ in range(t):
    n = int(input())
    c = 0
    while n > 0:
        if n - 4 >= 0:
            n -= 4
            c += 1
        elif n - 2 >= 0: 
            n -= 2
            c += 1
    print(c)