def generate(pos, length, cur, digits, nums):
    if pos == length:
        nums.append(int(cur))
        return

    for d in digits:
        if pos == 0 and length > 1 and d == 0:
            continue
        generate(pos + 1, length, cur + str(d), digits, nums)


t = int(input())

for _ in range(t):
    a, n = map(int, input().split())
    digits = list(map(int, input().split()))

    s = str(a)
    ans = 10**18

    for length in range(max(1, len(s) - 1), len(s) + 2):
        nums = []
        generate(0, length, "", digits, nums)
        for x in nums:
            ans = min(ans, abs(a - x))

    print(ans)