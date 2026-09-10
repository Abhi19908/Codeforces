ch = input()
s = input()
l1 = "qwertyuiop"
l2 = "asdfghjkl;"
l3 = "zxcvbnm,./"
ans = ""
if ch == 'R':
    for i in range(len(s)):
        if s[i] in l1:
            ans += l1[l1.index(s[i]) - 1]
        elif s[i] in l2:
            ans += l2[l2.index(s[i]) - 1]
        elif s[i] in l3:
            ans += l3[l3.index(s[i]) - 1]
elif ch == 'L':
    for i in range(len(s)):
        if s[i] in l1:
            ans += l1[l1.index(s[i]) + 1]
        elif s[i] in l2:
            ans += l2[l2.index(s[i]) + 1]
        elif s[i] in l3:
            ans += l3[l3.index(s[i]) + 1]
print(ans)