n = int(input().strip())
a = list(map(int, input().split()))

maxh = max(a)
minh = min(a)

# leftmost index of max
pos_max = a.index(maxh)

# rightmost index of min
# can find by rindex logic: scan from right
pos_min = n - 1 - a[::-1].index(minh)

if pos_max < pos_min:
    ans = pos_max + (n - 1 - pos_min)
else:
    ans = pos_max + (n - 1 - pos_min) - 1

print(ans)