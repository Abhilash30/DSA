n,t = map(int, input().split())
e = input()
s = []
count = 0
for j in e:
    s.append(j)
while t > 0:
    i = 0
    while i < len(s) - 1:
        if s[i] == "B" and s[i+1] == "G":
            s[i], s[i+1] = s[i+1], s[i]
            i += 2
        else:
            i += 1
    t -= 1

print("".join(s))
