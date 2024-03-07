n = int(input())
new = []
new.append(1)
new.append(n)
cnt = 1

while True :
    cnt += 1
    new.append(new[cnt-1] + new[cnt-2])
    if new[cnt] > 100 :
        break
        
for elem in new :
    print(elem, end=" ")