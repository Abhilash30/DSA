n = int(input())
l = list(map(int,input().split()))
count = 0
for i in range(n):
    if l[i] == 1:
         count += 1

if count >= 1:
     print("HARD")
else:
     print("EASY")