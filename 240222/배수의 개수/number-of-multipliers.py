three = 0
five = 0

for _ in range(10) :
    a = int(input())
    if a%3 ==0 :
        three += 1
    
    if a%5 == 0 :
        five += 1

print(three, end=" ")
print(five)