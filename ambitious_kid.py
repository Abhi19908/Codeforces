n = int(input())
a = list(map(int, input().split()))
min = abs(a[0])
if 0 in a:
    print(0)
else:
    for i in a:
        if abs(i) < min:
            min = abs(i)
    print(min)