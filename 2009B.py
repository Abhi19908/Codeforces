t = int(input())
for _ in range(t):
    n = int(input())
    l = [] 
    for i in range(n):
        s = input()
        for j in range(len(s)):
            if s[j] == '#':
                l.append(j+1)
                break
    l.reverse()
    print(*l)