n = int(input())
has_three = False
sol = []
res = []
temp = 1;

for j in range(1,1000):
        temp = j
        while temp > 0:
            if temp%10 == 3:
                has_three = True
            temp /= 10

        if j % 3 != 0 and has_three == False:
            sol.append(j)
print(sol)
for i in range(n):
    k = int(input())
    #res.append(sol[k])
    
   
print(res)
