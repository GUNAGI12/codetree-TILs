inp = input().split()
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])

if b>a : # a b
    if b<c : # a b c
        print(b)
    elif a<c : # a c b
        print(c)
    else :
        print(a)
else : # b a
    if a<c : # b a c
        print(a)
    elif b<c : # b c a
        print(c)
    else : # b a
        print(b)


        #b ca