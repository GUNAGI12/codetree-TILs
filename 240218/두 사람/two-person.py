inp = input()
first = inp.split()
fage = int(first[0])
fsex = first[1]

inp = input()
sec = inp.split()
sage = int(sec[0])
ssex = sec[1]

if (fage>=19 and fsex == "M") or (sage >= 19 and ssex == "M") :
    print("1")

else : 
    print("0")