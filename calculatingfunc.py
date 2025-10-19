import sys
n = int(sys.stdin.readline().strip())
if n % 2 == 0:
    print(n // 2)
else:
    print(- (n + 1) // 2)