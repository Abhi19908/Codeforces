t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    f = True
    for i in range(n):
        if a[i] != b[i]:
            if a[i] in ('G', 'B') and b[i] in ('G', 'B'):
                f = True
            else:
                f = False
                break

    print("Yes" if f else "No")