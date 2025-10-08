n, k = map(int, input().split())


if n > 10:
    while k > 0:
        l = []
        s = str(n)
        for i in s:
            l.append(int(i))

        if l[len(l) - 1] == 0:
            n = n//10
            n += 1
        n = n - 1
        k -= 1
else:
    while k > 0:
        n = n - 1
        k -= 1


print(n)