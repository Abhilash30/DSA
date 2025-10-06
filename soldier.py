k,n,w = map(int,input().split())

i = 0

for j in range(1,w+1):
    i += j*k

if i > n:
    i = i - n
    print(i)
else:
    print("0")