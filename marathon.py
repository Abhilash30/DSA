n = int(input())
count = 0
sol = []
for i in range(n):
    a = list(map(int,input().split()))
    for j in range(len(a)):
        if a[0] < a[j]:
            count += 1
            
    sol.append(count)
    count = 0

for k in sol:
    print(k)
