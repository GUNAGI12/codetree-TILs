arr = list(map(int, input().split()))

for i in range (100) :
    if arr[i] == 0 :
        k = i
        break

print(arr[k-1] + arr[k-2] + arr[k-3])