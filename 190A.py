t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())

    if 3 * a <= b:
        print(n * a)
    else:
        full_groups = n // 3
        leftovers = n % 3
        cost = (full_groups * b) + min(leftovers * a, b)
        print(cost)