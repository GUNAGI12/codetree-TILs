sum_val = 0
cnt = 0

for i in range(10) :
    a = int(input())
    if a>=0 and a<= 200 :
        sum_val += a
        cnt += 1
avg = sum_val/cnt
print(sum_val, f"{avg:.1f}")