a = []
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    
    

    if max(a) - min(a) <= 1:
        a.append("YES")
    else:
        a.append("NO")

for i in a:
    print(i)