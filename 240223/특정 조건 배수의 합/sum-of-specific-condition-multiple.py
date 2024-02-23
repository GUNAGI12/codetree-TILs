inp = input().split()
a, b = int(inp[0]), int(inp[1])

s = 0
if(a<=b) :
    for i in range (a, b+1) :
        if i%5 == 0 :
            s += i

else :
    for i in range (b, a+1) :
        if i%5 == 0 :
            s += i
print(s)