inp = input().split()
a, b = int(inp[0]), int(inp[1])

if a>=b :
    for i in range (a, b-1, -1) :
        print(i, end=" ")
else :
    for ii in range(b, a-1, -1) :
        print(ii, end=" ")