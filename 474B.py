n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))
l = []
c = 0
for i in a:
    c += 1
    for j in range(i):
        l.append(c)
for i in q:
    print(l[i-1])