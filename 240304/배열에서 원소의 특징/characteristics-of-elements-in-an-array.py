arr = list(map(int,input().split()))

for i in range(0,9) :
    if arr[i] % 3 == 0 :
        k = i
        break

print(arr[k-1])