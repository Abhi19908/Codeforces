n = int(input())
k=[4 , 7, 44, 47, 74, 77, 444, 447, 474, 477, 777, 744, 747, 774]
l = list(str(n))
if n %4 == 0 or n % 7 == 0:
    print("YES")
else:
    for i in k:
        if n % i == 0:
            print("YES")
            exit()
    print("NO")
    