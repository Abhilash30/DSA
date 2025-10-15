n = int(input())
count = 0
counts = []

for i in range(n):
    a, b = map(int, input().split())
    count += b - a
    counts.append(count)

print(max(counts))

    

