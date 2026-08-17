n,m,a,b = map(int, input().split())
travel_a = n * a
c = n // m
travel_b = b * c
multiple = travel_b
if(n - c * m > 0): 
    multiple += b
    travel_b += (n - c * m) * a
print(min(travel_a,travel_b,multiple))