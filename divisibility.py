import sys

data = list(map(int, sys.stdin.buffer.read().split()))
t = data[0]
out = []
idx = 1

for _ in range(t):
    a = data[idx]
    b = data[idx+1]
    idx += 2
    # assume b > 0 (division by zero is undefined)
    out.append(str((b - a % b) % b))

sys.stdout.write("\n".join(out))



    
