n = int(input())

nums = [1, 5, 10, 20, 100]
count = 0

for i in reversed(nums):
    count += n//i
    n = n % i

print(count)