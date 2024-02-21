inp = input().split()
c, n = inp[0], int(inp[1])

if c == "A" :
    for i in range(1, n+1) :
        print(i, end=" ")

else :
    for ii in range(n, 0, -1) :
        print(ii, end=" ")