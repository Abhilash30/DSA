#n, k, l, c, d, p, nl, np
n, k, l, c, d, p, nl, np = map(int, input().split())
total_toasts = min((k*l)//nl, c*d, p//np)
print(total_toasts // n)