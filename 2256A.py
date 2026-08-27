t = int(input())
for _ in range(t):
    a,b,c = map(int, input().split())
    max_value = max(a,b,c)
    min_value = min(a,b,c)
    mid_value = a + b + c - max_value - min_value
    min_range = max_value - min_value
    min_range = min(min_range, (mid_value + min_value) - min_value)
    print(min_range)