# n = int(input())
# count = 0
# for i in str(n):
#     if i == "4" or i == "7":
#         count += 1


# if n % 4 == 0 or n%7 ==0 or count == len(str(n)):
#     print("YES")
# else:
#     print("NO")

n = int(input())
lucky_nums = [4, 7, 44, 47, 74, 77, 444, 447, 474, 477, 744, 747, 774, 777]

for x in lucky_nums:
    if n % x == 0:
        print("YES")
        break
else:
    print("NO")