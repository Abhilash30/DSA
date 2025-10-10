n = int(input())
s = input()
l = []
count = 0

for i in s:
    if i == "A":
        l.append(i)
    else:
        count += 1

if count > len(l):
    print("Danik")
elif count < len(l):
    print("Anton")
else:
    print("Friendship")
