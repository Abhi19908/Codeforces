n = int(input())
l = list(str(n))
for i in range(len(l)):
    if l[i] == '9' and i == 0: # if the first digit is 9 we keep it as 9
        continue
    l[i] = int(min(int(l[i]), 9 - int(l[i]))) # choose the minimum between the digit and 9 - digit
print(''.join(map(str,l))) # print the list as a string