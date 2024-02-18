inp = input().split()
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])

if b>a :
    if b<c :
        print(b)
    else :
        print(c)
else :
    if a<c :
        print(a)
    else :
        print(c)

        #b ca