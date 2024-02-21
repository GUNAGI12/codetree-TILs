inp = input().split()
a, b = int(inp[0]), int(inp[1])

i = a
while i<=b :
    print(i, end=" ")
    if i%2 != 0 :
        i *=2

    else :
        i += 3