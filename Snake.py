n,m = map(int, input().split())

count = 0

for i in range(0,int(n)): 
        if i%2 == 0:
            print("#"*m)
        if i%2 != 0 and count%2 == 0:
            print("."*(m-1) + "#")
            count += 1
        elif i%2 != 0 and (count%2 != 0 or count == 1):
            print("#" + "."*(m-1))
            count += 1



