a,b = map(int, input().split())

year = 0

for i in range(20):
    year += 1
    a = a * 3
    b = b *2
    if a > b:
        print(year)
        break

