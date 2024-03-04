arr = list(map(int, input().split()))
sum1 = 0
sum2 = 0
for i in range(0, 9, 2) :
    sum1 += arr[i]

for ii in range(1,9,2) :
    sum2 += arr[ii]

if sum1 > sum2 :
    print(sum1 - sum2)
else :
    print(sum2-sum1)