t = int(input())
for _ in range(t):
    s = list(input())
    c = s.count('4')
    t2 = s.count('2')
    min = cd = t2
    for i in s:
        if i == '2':
            cd -= 1
        elif i == '1' or i == '3':
            cd += 1
        if cd < min:
            min = cd
    print(c+min)