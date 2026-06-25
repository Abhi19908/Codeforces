n = int(input())

for _ in range(n):
    k = int(input())
    s = list(input())
    tot = 0
    l = [False] * 26
    for i in s:
        c = ord(i) - ord('A')
        if l[c]:
            tot += 1
        else:
            
            l[c] = True
            tot += 2
    print(tot)
