t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    l = sorted(list(s))
    print(ord(l[-1]) - ord('a') + 1)