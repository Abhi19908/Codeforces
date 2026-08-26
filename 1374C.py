t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a,c = 0,0
    for i in range(n):
        if s[i] == '(':
            c += 1
        else:
            c -= 1
            if c < 0:
                a += 1
                c = 0

    print(a)