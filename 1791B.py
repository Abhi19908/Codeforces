t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    i,j = 0,0
    for c in s:
        if i == 1 and j == 1:
            break
        if c == 'U':
            i += 1
        elif c == 'D':
            i -= 1
        elif c == 'L':
            j -= 1
        elif c == 'R':
            j += 1
    if i == 1 and j == 1:
        print("YES")
    else:
        print("NO")