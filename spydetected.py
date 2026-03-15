t = int(input())
sol = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Determine the common value
    if a[0] == a[1] or a[0] == a[2]:
        common = a[0]
    else:
        common = a[1]

    # Find and print the index (1-based)
    for i in range(n):
        if a[i] != common:
            sol.append(i+1)
            break

for i in sol:
    print(i)