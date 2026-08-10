s = input()
c = 0
for i in s:
    if i.isupper():
        c+= 1
if c == len(s) - 1 and s[0].islower():
    s = s[0].upper() + s[1:].lower()
elif c == len(s):
    s = s.lower()
print(s)