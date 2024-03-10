n,q = map(int,input().split())
arr = list(map(int,input().split()))

for _ in range(q) :
    qu = list(map(int,input().split()))

    if qu[0] == 1 :
        a = qu[1]
        print(arr[a-1])

    elif qu[0] == 2 :
        a = qu[1]
        idx = -1
        if a in arr :
            idx = arr.index(a)
        print(idx + 1)
    else :
        a = qu[1]
        b = qu[2]
        for i in range(a-1, b) :
            print(arr[i], end=" ")
        print()