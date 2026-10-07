t = int(input())
for _ in range(t):
    n,a,b = map(int, input().split())
    if a * 2 <= b:
        print(n * a)
    else:
        x = n // 2
        y = n % 2
        print(x * b + y * a)