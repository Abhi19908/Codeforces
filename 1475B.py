t = int(input())
for _ in range(t):
    n = int(input())
    y = n % 2020
    x = (n - y) // 2020 - y
    if x >= 0 and y >= 0:
        print("YES")
    else:
        print("NO")