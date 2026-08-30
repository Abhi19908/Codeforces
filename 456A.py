n = int(input())
pr = []
ql = []
for i in range(n):
    p, q = map(int, input().split()) #i input for every computer
    pr.append(p)
    ql.append(q)
f = False
for i in range(n):
    if pr[i] != ql[i]: # if they are not equal then conditon is satisfied
        f = True
        break
if f:
    print("Happy Alex")
else:
    print("Poor Alex")