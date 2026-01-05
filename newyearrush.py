# n, k = map(int, input().split())
# count = 0
# time_net = 240 - k
# for i in range(1,n+1):
#     count += i*5
#     if(count > time_net):
#         n = i - 1
#         break


# print(n)
#^ is O(n) but the answer below is O(1) through math!
import math

n, k = map(int, input().split())
time_left = 240 - k

# Solve x^2 + x - 2*time_left/5 <= 0
x = int(( -1 + math.sqrt(1 + 8 * time_left // 5) ) // 2)

print(min(x, n))
