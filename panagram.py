# t = int(input())
# letters = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# st = input()
# c = []
# for i in st.lower():
#     if i in letters:
#         c.append(i)
#     else:
#         break
# if len(set(c)) == len(letters): 
#     print("YES")
# else:
#     print("NO")
#Faster code given bellow
import sys
from string import ascii_lowercase

input_data = sys.stdin.read().splitlines()
t = int(input_data[0])
lines = input_data[1:]

for i in range(t):
    s = lines[i]
    letters_seen = {ch for ch in s.lower() if ch.isalpha()}
    print("YES" if len(letters_seen) == 26 else "NO")