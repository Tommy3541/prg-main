pin = 5234
i=0
while True:
    i+=1
    kod = int(input("zadej "))
    if kod == pin:
        print("vyhra") 
        break
    elif i > 3:
        print("konec")
        break
    elif kod > 5134 and kod < 5334:
        print("blizko")
    elif kod > 4234 and kod < 6234:
        print("skoro blizko")
    else:
        print("spatne")
