n,m = map(int, input().split())
c = (n + 1) // 2
a = (c + m - 1) // m * m
print(a if a <= n else -1)