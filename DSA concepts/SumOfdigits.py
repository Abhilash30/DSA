# def SumOfDigits(num):
#     count = 0
#     for i in range(1,num+1):
#         count += i
#     return count # O(n)
def SumOfDigits(n):
  return n(n+1)//2 #O(1)
print(SumOfDigits(input("Enter a number: ")))