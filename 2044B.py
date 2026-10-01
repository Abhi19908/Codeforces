t = int(input())
for _ in range(t):
    s = input()
    a = ""
    for i in range(len(s)-1,-1,-1):
        if s[i] == 'p':
            a += 'q'
        elif s[i] == 'q':
            a += 'p'
        else:
            a += s[i]
    print(a)