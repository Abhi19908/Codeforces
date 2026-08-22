t = int(int(input()))
for _ in range(t):
    x,y = map(int, input().split())
    print(min(x,y),max(y,x))