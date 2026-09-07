t = int(input())
for _ in range(t):
    n = int(input())
    s = 0
    m,c = 0,0
    for x in range(2,n+1): # check till n
        j = 1
        while (x * j) <= n: 
            s += x * j # check sum until less than n
            j += 1
        if s > m: # if greater choose it
            m = s
            c = x
        s = 0
    print(c)