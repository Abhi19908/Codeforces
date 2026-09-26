t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    m = min(max(2 * a, b), max(2 * b, a))
    print(m ** 2)