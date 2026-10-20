t = int(input())
for _ in range(t):
    s = ""
    for _ in range(8):
        t = input()
        for i in t: 
            if i != ".":
                s += i
    print(s)