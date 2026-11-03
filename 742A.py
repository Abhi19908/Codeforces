n = int(input())
c = n % 4
if n == 0:
    print(1)
    exit()
match c:
    case 0:
        print(6)
    case 1:
        print(8)
    case 2:
        print(4)
    case 3: 
        print(2)
