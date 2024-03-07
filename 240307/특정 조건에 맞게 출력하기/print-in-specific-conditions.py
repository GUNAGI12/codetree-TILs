arr = list(map(int, input().split()))
new = []

for i in range(100) :
    if arr[i] == 0 :
        break
    if arr[i] %2 == 0 :
        new.append(arr[i] // 2)

    else :
        new.append(arr[i] + 3)

for elem in new :
    print(elem, end=" ")