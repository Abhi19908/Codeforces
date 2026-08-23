t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    req = (k - 1) // (n - 1)
    print(k+req)