n = input()
l = []
for i in n:
    l.append(int(i))

if l.count(7) + l.count(4) == 7 or l.count(7) + l.count(4) == 4:
    print("YES")
else:
    print("NO")