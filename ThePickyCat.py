import sys

input_data = sys.stdin.read().strip().split()
it = iter(input_data)
t = int(next(it))

out_lines = []
for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    abs_pairs = [(abs(a[i]), i) for i in range(n)]
    abs_pairs.sort()  # sort by absolute value ascending
    # mark indices whose abs-values are among smallest floor(n/2)+1
    allowed = set(idx for _, idx in abs_pairs[:(n // 2) + 1])
    out_lines.append("YES" if 0 in allowed else "NO")

print("\n".join(out_lines))
        

    

