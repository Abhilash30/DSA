l = list(map(int, input().split()))
ans = set(l)
disth = len(ans)
acth = len(l)
diff = acth - disth
print(diff)
