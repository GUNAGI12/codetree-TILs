inp = input().split()
a, b = int(inp[0]), int(inp[1])

while a<=b :
    if a%2 == 0 :
        print(a, end=" ")
    a += 1