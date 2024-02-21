inp = input().split()
a, b = int(inp[0]), int(inp[1])

if a>0 :
    for i in range(1, b+1) :
        print(a, end="")

else :
    print("0")