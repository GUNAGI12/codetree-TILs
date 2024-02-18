inp = input()
a = inp.split()
amath = int(a[0])
aeng = int(a[1])

inp = input()
b = inp.split()
bmath = int(b[0])
beng = int(b[1])

if amath>bmath or (amath == bmath and aeng > beng) :
    print("A")

else :
    print("B")