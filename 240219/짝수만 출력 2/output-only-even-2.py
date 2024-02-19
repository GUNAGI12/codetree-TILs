inp = input().split()
b, a = int(inp[0]), int(inp[1])

while b>=a :
    if b%2 == 0 :
        print(b, end=" ")
    b += -1