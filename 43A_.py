t = int(input())
d = {}
for _ in range(t):
    s = input()
    if s in d:
        d[s] += 1
    else:
        d[s] = 1
m = ""
for k, v in d.items():
    if v > d.get(m, 0):
        m = k
print(m)