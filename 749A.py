n = int(input())
l = [] 
if n & 1:
    n -= 1
    while n > 0:
        l.append(2)
        n -= 2
    l[-1] = 3
else:
    while n > 0:
        l.append(2)
        n -= 2
print(len(l))
print(*l)