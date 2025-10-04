n = int(input())
s = str(input())
l = []
count = 0
for i in s:
        l.append(i)
for j in range(n-1):
        if l[j] == l[j+1]:
            count +=1
        

print(count)