t = int(input())
sol = []

for i in range(t):
    n = int(input())

    if ((n + 1) % 3 == 0 or (n - 1) % 3 == 0):
        sol.append("First")
    else:
        sol.append("Second")


for ans in sol:
    print(ans)

