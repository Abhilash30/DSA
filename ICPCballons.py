n = int(input())
freq = {}
count = 0
sols = []
for i in range(n):
    s = str(input())
    for j in s:
        if j in freq:
            freq[j] += 1
            count += 1
        else:
            freq[j] = 1
            count += 2
    sols.append(count)
    freq.clear()
    count = 0

for j in sols:
    print(j)
