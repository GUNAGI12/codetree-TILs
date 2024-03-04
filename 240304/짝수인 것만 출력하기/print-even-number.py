n = int(input())
arr = list(map(int, input().split()))
new = []

for elem in arr :
    if elem % 2 == 0 :
        new.append(elem)

for elem in new :
    print(elem, end=" ")