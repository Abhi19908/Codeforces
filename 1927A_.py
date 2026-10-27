t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    i,j = 0, n-1
    while i < j:
        if s[i] != 'B':
            i += 1
        elif s[j] != 'B':
            j -= 1
        else:
            break
    print(j - i + 1)