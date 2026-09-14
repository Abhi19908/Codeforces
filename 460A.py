n,m = map(int ,input().split())
c = n
c += (n - 1) // (m - 1) # divides to get max socks
print(c)