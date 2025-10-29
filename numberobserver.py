l = input()
l1 = []
c = input()
c1 = []
ans = []
for i in l:
    l1.append(i)
    c1.append(i)

for i in range(len(l1)):
    if l[i] != c[i]:
        ans.append(1)
    else:
        ans.append(0)

print("".join(map(str,ans)))