k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())
l = [k, l, m, n]
a = []
flist = []
i = 0
for p in range(1,d+1):
    flist.append(p)

# while i < 4:
#     for j in range(1, d+1, l[i]):
#         a.append(j)
#     i += 1
for j in l:
    num = j
    for i in range(1,d+1):
        new_num = num * i
        if new_num > d:
            break
        a.append(new_num)
        


b = list(set(a))
b.sort()
damaged_dragons = len(b)
print(flist)
if b == flist:
    print(d)
else:
    print(damaged_dragons)