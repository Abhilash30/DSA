# n = int(input())
# a = set(map(int, input().split()))
# b = set(map(int, input().split()))
# if 0 in a or 0 in b:
#     n += 1
# c = set(a.union(b))
# if len(c) == n:
#     print("I become the guy.")
# else:
#     print("Oh, my keyboard!")
# Understand the question correctly

n = int(input())

# Read player X's levels
x = list(map(int, input().split()))
# Read player Y's levels
y = list(map(int, input().split()))

# Remove the first element (count)
a = set(x[1:])
b = set(y[1:])

# Combine both sets
c = a.union(b)

if len(c) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")

