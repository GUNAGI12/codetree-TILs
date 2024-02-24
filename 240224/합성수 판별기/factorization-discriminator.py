n = int(input())
satisfied = False

for i in range(2, n+1) :
    if n%i == 0 :
        satisfied = True

    else :
        satisfied = False

if satisfied == True :
    print("C")
else :
    print("N")