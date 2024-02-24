inp = input().split()
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])
satisfied = False
for i in range(a, b+1) :
    if c%i != 0 :
        satisfied = True

if satisfied == True :
    print("YES")

else :
    print("NO")