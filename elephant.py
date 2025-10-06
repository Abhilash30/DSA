n = int(input())
count = 0
l = []
a=0
while n>=5:
    a=n-5
    n-=5
    l.append(a)
    if a<=5:
        break
a = n
for i in range(1,6):
    if i==a:
        l.append(i)
        

print(len(l))