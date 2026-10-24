s = input()
l = list(s)
c = min(ord(l[0]) - ord('a'),26 - (ord(l[0]) - ord('a')))
for i in range(1, len(l)):
    c += min(abs(ord(l[i]) - ord(l[i-1])), 26 - abs(ord(l[i]) - ord(l[i-1])))
print(c)