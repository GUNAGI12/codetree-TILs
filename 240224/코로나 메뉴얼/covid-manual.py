inp = input()
a = inp.split()
asym = a[0]
atem = int(a[1])

inp = input()
b = inp.split()
bsym = b[0]
btem = int(b[1])

inp = input()
c = inp.split()
csym = c[0]
ctem = int(c[1])

if ((asym == "Y" and atem >=37) and (bsym == "Y" and btem >= 37)) or ((asym == "Y" and atem >=37) and (csym == "Y" and ctem >=37)) or ((bsym == "Y" and btem>=37) and (csym == "Y" and ctem >=37)) :
    print("E")

else :
    "N"