t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    ones = 0
    others = 0
    cap = 0

    for x in a:
        if x == 1:
            ones += 1
        else:
            others += x
            if x > 3:
                cap += (x - 2) // 2

    if ones + others < 3:
        print(0)
    elif cap >= ones:
        print(ones + others)
    else:
        if ones == n - 1:
            print(others + cap + 1)
        else:
            print(others + cap)