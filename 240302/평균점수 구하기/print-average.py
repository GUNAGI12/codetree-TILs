arr = list(map(float, input().split()))
sum_val = 0

for elem in arr :
    sum_val += elem

avg = sum_val / 8

print(f"{avg:.1f}")