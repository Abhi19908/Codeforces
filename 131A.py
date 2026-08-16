s = input()
c = 0
for i in s:
    if i.isupper(): # checl how many are upper
        c+= 1
if c == len(s) - 1 and s[0].islower(): # if first letter is lower and rest are upper
    s = s[0].upper() + s[1:].lower() 
elif c == len(s): # if all are capital
    s = s.lower()
print(s)
