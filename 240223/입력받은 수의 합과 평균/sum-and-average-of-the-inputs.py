n = int(input())

sum_val = 0
cnt = 0

for i in range (n) :
    score = int(input())
    sum_val += score
avg = sum_val/n

print(sum_val, f"{avg:.1f}")