inp = input().split()
a, b, c = int(inp[0]), int(inp[1]), int(inp[2])
satisfied = True
for i in range(a, b+1) :
    if i%c == 0 :
        satisfied = False

if satisfied == True :
    print("YES")

else :
    print("NO")