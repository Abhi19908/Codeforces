a = int(input())
la = list(map(int, input().split()))
b = int(input())
lb = list(map(int, input().split()))
la.sort()
lb.sort()
i, j = a-1, b-1
c = 0
while i >= 0 and j >= 0:
    if abs(la[i] - lb[j]) <= 1:
        c += 1
        i -= 1
        j -= 1
    else:
        if la[i] > lb[j]:
            i -= 1
        else:
            j -= 1
print(c)