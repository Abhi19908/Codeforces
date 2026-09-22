n = int(input())
l = list(map(int,input().split()))
d = [0] * 100001
for i in l:
    d[i] += 1
f = [0] * 100001
f[1] = d[1]
for i in range(2,100001):
    f[i] = max(f[i-1],f[i-2] + d[i] * i)
print(f[100000])