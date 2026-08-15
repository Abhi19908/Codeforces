t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    # to count teh numbers in the card
    ones = 0 
    others = 0
    cap = 0 # extra members

    for x in a:
        if x == 1:
            ones += 1
        else:
            others += x
            if x > 3: 
                cap += (x - 2) // 2 # rounding off 

    if ones + others < 3: # simply imposible
        print(0)
    elif cap >= ones: # just enough to fulfill condition
        print(ones + others)
    else: # not enough
        if ones == n - 1: # if all are one tehn there is extra space
            print(others + cap + 1)
        else:
            print(others + cap)
