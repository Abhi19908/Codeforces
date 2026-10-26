n = int(input())
s = input()
d = {}
for i in range(n-1):
    a = s[i:i+2]
    if a in d:
        d[a] += 1
    else:
        d[a] = 1
print(max(d.items(), key =lambda x: x[1])[0])