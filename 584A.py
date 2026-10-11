n,t = map(int,input().split())
s = [0] * n
s[0] = 1
k = ''.join(str(x) for x in s)
k = int(k)
for i in range(k,k * 10):
    if i % t == 0:
        print(i)
        exit()
print(-1)