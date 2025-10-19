n = int(input())
count = 0
for i in range(n):
    a = list(map(int, input().split()))
    p = a[1] - a[0]
    if a[0]<=a[1] and p >= 2:
       count += 1           
print(count)