n = int(input())
for i in range (n, 101, 1) :
    if i<60 :
        print("F", end=" ")
    elif i<70 :
        print("D", end=" ")
    elif i<80 :
        print("C", end=" ")
    elif i<90 :
        print("B", end=" ")
    else :
        print("A", end=" ")