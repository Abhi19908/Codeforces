m,n = map(int,input().split())
l = [list(map(str,input().split())) for _ in range(m)]
d = ['C', 'M', 'Y']
f = False
for i in range(m):
    for j in range(n):
        if l[i][j] in d:
            f = True
            break
print("#Color" if f else "#Black&White")