t = int(input())
for _ in range(t):
    n = int(input())
    for i in range(2,31):
        s = pow(2,i) - 1
        if n % s == 0:
            print(n // s)
            break