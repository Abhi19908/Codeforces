s = input()
t = int(input())
sm = [0] * (len(s))
for i in range(1, len(s)):
    sm[i] = sm[i-1]
    if s[i] == s[i-1]:
        sm[i] += 1
for _ in range(t):
    l, r = map(int, input().split())
    print(sm[r-1] - sm[l - 1])