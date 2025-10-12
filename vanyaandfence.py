n, h = map(int, input().split())
heights = list(map(int, input().split()))
w = []
for i in range(n):
    w.append(1)
    if heights[i] > h:
        w.append(1)
    
print(sum(w))
