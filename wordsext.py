s = input()
upper = []
lower = []
for i in s:
    if i.isupper() == True:
        upper.append(i)
    else:
        lower.append(i)

if len(upper)>len(lower):
    print(s.upper())
else:
    print(s.lower())